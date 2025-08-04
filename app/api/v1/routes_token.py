from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.base import engine
from app.models.token import Token
from app.models.user import User
from datetime import datetime, timezone
from jose import jwt, JWTError
from app.core.config import settings
from app.crud.token import create_access_token, create_refresh_token
from app.core.role_scopes import role_scope_map

router = APIRouter()

SECRET_REFRESH_KEY = settings.SECRET_REFRESH_KEY
ALGORITHM = settings.ALGORITHM


@router.get('/refresh')
def refresh_token_route(refresh_token: str):

    if not SECRET_REFRESH_KEY or not ALGORITHM:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Server misconfiguration: missing SECRET or ALGORITHM'
        )

    try:
        payload = jwt.decode(
            refresh_token, SECRET_REFRESH_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('user_id')

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid payload')

    except JWTError:
        raise HTTPException(
            status_code=401, detail='Invalid refresh token')

    with Session(engine) as session:

        # Check if token exists in db
        stmt = select(Token).where(Token.token == refresh_token)
        token = session.execute(stmt).scalar_one_or_none()

        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not recognized')

        if token.expiry_time < int((datetime.now(timezone.utc)).timestamp()):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired in db')

        # Get related user
        stmt = select(User).where(User.id == user_id)
        user = session.execute(stmt).scalar_one_or_none()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='No user found for token')
        

        # Issue new tokens
        scopes = role_scope_map[user.role]
        new_access_token = create_access_token(user, scopes)
        new_refresh_token = create_refresh_token(user)

        session.commit()

        return {'access_token': new_access_token, 'refresh_token': new_refresh_token, 'token_type': 'bearer'}
