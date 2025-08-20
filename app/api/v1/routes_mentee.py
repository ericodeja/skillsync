from fastapi import APIRouter, Security
from app.schemas.mentee import Mentee, MenteeUpdate
from app.crud.mentee import create_mentee, update_mentee
from app.schemas.user import UserBase
from app.auth.auth import get_current_user



router = APIRouter()


@router.post('/')
def create_mentee_route(mentee_data: Mentee, user: UserBase = Security(get_current_user, scopes=["write:profile"])):
    new_mentee = create_mentee(user, mentee_data)
    return new_mentee

@router.patch('/')
def update_mentee_route(update_info: MenteeUpdate, user: UserBase = Security(get_current_user, scopes=["write:profile"])):
    updated_mentor = update_mentee(user, update_info)
    return updated_mentor