from fastapi import APIRouter, Security
from app.crud.mentor import create_mentor
from app.schemas.mentor import Mentor, MentorUpdate
from app.auth.auth import get_current_user
from app.schemas.user import UserBase
from app.crud.mentor import update_mentor


router = APIRouter()

@router.post('/')
def create_mentor_route(mentor_data: Mentor,  user: UserBase = Security(get_current_user, scopes=["write:profile"])):
    new_mentor = create_mentor(user, mentor_data)
    return new_mentor


@router.patch('/')
def update_mentor_route(update_info: MentorUpdate, user: UserBase = Security(get_current_user, scopes=["write:profile"])):
    updated_mentor = update_mentor(user, update_info)
    return updated_mentor