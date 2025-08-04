from fastapi import APIRouter
from app.crud.user import create_user
from app.schemas.user import User, UserBase

router = APIRouter()


@router.post('/', response_model=UserBase)
def create_user_route(user_data: User):
    new_user = create_user(user_data)
    return new_user
