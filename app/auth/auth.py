from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import SecurityScopes
from app.db.base import engine
from app.models.user import User
from app.schemas.user import UserBase
from app.core.security import verify_password
from app.core.dependencies import oauth2_scheme
from jose import jwt, JWTError
from app.core.config import settings
from typing import List


SECRET_ACCESS_KEY = settings.SECRET_ACCESS_KEY
ALGORITHM = settings.ALGORITHM


def authenticate_user(req_email, req_password):
    with Session(engine) as session:
        stmt = select(User).where(User.email == req_email)
        user = session.execute(stmt).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with {req_email} not found.")

        if not verify_password(req_password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')

        return user


def decode_token(token):
    try:
        if not SECRET_ACCESS_KEY:
            raise ValueError("Missing SECRET_ACCESS_KEY")

        if not ALGORITHM:
            raise ValueError("Missing ALGORITHM")

        payload = jwt.decode(token, SECRET_ACCESS_KEY, algorithms=[ALGORITHM])

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')


def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    id = payload.get('user_id')
    token_scopes: List[str] = payload.get("scopes", [])

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    if id is None:
        raise credentials_exception
    
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
            )
    
    with Session(engine) as session:
        stmt = select(User). where(User.id == id)
        user = session.execute(stmt).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist")

        return UserBase(id=user.id, username = user.first_name, role = user.role)
