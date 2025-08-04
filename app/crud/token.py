from app.schemas.user import UserBase
from datetime import datetime, timezone, timedelta
from jose import jwt # type: ignore
from app.core.config import settings
from app.models.token import Token
from sqlalchemy.orm import Session
from app.db.base import engine

SECRET_ACCESS_KEY = settings.SECRET_ACCESS_KEY
SECRET_REFRESH_KEY = settings.SECRET_REFRESH_KEY
ALGORITHM = settings.ALGORITHM


def create_access_token(user, scopes: list):
    encode = {'id': user.id}

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
    encode = {'id': user.id}
    expires = datetime.now(timezone.utc) + timedelta(minutes=7)
    encode['exp'] = int(expires.timestamp())

    
    if not SECRET_REFRESH_KEY:
        raise ValueError("Missing SECRET_REFRESH_KEY")

    if not ALGORITHM:
        raise ValueError("Missing ALGORITHM")
    

    #Create refresh token
    refresh_token = jwt.encode(
        encode, SECRET_REFRESH_KEY, algorithm=ALGORITHM)

    #Insert into database
    with Session(engine) as session:
        new_token = Token(
            token=refresh_token,
            user_id=user.id
        )
        session.add(new_token)
        session.commit()

    return refresh_token
    

