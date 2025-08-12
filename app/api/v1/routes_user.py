from fastapi import APIRouter, HTTPException, status
from app.crud.user import create_user, delete_user
from app.schemas.user import User, UserBase
from fastapi import Security
from app.auth.auth import get_current_user

router = APIRouter()


@router.post('/', response_model=UserBase)
def create_user_route(user_data: User):
    new_user = create_user(user_data)
    return new_user

@router.delete('/')
def delete_user_route(user: UserBase = Security(get_current_user, scopes=["write: profile"])):
    delete_user(user)