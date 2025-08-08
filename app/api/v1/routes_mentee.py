from fastapi import APIRouter
from app.schemas.mentee import Mentee
from app.crud.mentee import create_mentee



router = APIRouter()


@router.post('/')
def create_mentee_route(mentee_data: Mentee):
    new_mentee = create_mentee(mentee_data)
    return new_mentee