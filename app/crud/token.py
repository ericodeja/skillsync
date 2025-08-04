from fastapi import HTTPException, status
from datetime import datetime, timezone, timedelta
from jose import jwt
from app.core.config import settings
from app.models.token import Token
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.base import engine

SECRET_ACCESS_KEY = settings.SECRET_ACCESS_KEY
SECRET_REFRESH_KEY = settings.SECRET_REFRESH_KEY
ALGORITHM = settings.ALGORITHM


def create_access_token(user, scopes: list):
    encode = {'user_id': user.id}

    encode['scopes'] = ' '.join(scopes)
    expires = datetime.now(timezone.utc) + timedelta(minutes=15)
    encode['exp'] = int(expires.timestamp())

    if not SECRET_ACCESS_KEY:
        raise ValueError("Missing SECRET_ACCESS_KEY")

    if not ALGORITHM:
        raise ValueError("Missing ALGORITHM")

    access_token = jwt.encode(
        encode, SECRET_ACCESS_KEY, algorithm=ALGORITHM)
    return access_token


def create_refresh_token(user):
    encode = {'user_id': user.id}
    expires = datetime.now(timezone.utc) + timedelta(days=7)
    encode['exp'] = int(expires.timestamp())

    if not SECRET_REFRESH_KEY or not ALGORITHM:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Server misconfiguration: missing SECRET or ALGORITHM'
        )

    # Create refresh token
    refresh_token = jwt.encode(
        encode, SECRET_REFRESH_KEY, algorithm=ALGORITHM)

    # Insert into database
    with Session(engine) as session:

        # Get and delete old_token if it exists
        stmt = select(Token).where(Token.user_id == user.id)
        old_token = session.execute(stmt).scalar_one_or_none()

        if old_token is not None:
            session.delete(old_token)

        # Create new refresh token
        new_token = Token(
            token=refresh_token,
            expiry_time=encode.get('exp'),
            user_id=encode.get('user_id')
        )
        session.add(new_token)
        session.commit()

    return refresh_token


def delete_refresh_token(user_id):
    with Session(engine) as session:
        stmt = select(Token).where(Token.user_id == user_id)
        token = session.execute(stmt).scalar_one_or_none()
        session.delete(token)
        session.commit()
