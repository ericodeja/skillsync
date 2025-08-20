from fastapi import HTTPException, status
from app.db.base import engine
from sqlalchemy import update
from sqlalchemy.orm import Session
from app.models.mentor import Mentor


def create_mentor(user,mentor_data):
    with Session(engine) as session:
        if user.role != "Mentor":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized profile')
        new_mentor = Mentor(
            user_id=mentor_data.user_id,
            bio=mentor_data.bio,
            years_of_experience=mentor_data.years_of_experience,
            timezone=mentor_data.timezone,
            available_hours=mentor_data.available_hours,
            skills=mentor_data.skills,
            rating=mentor_data.rating,
        )
        session.add(new_mentor)
        session.commit()

        return new_mentor
    
def update_mentor(user, update_info):
    with Session(engine) as session:
        update_data = update_info.dict(exclude_unset=True, exclude_none=True)

        if not update_data:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid update request')
        
        stmt = (
            update(Mentor)
            .where(Mentor.user_id == user.id)
            .values(**update_data)
            .returning(Mentor)
        )

        result = session.execute(stmt)
        updated_mentor = result.scalar_one_or_none()

        if not updated_mentor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Mentor profile not found')
        
        return updated_mentor