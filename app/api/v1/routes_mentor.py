from fastapi import APIRouter
from app.crud.mentor import create_mentor
from app.schemas.mentor import Mentor


router = APIRouter()

@router.post('/')
def create_mentor_route(mentor_data: Mentor):
    new_mentor = create_mentor(mentor_data)
    return new_mentor