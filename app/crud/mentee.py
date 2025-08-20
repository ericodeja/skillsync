from fastapi import HTTPException, status
from app.db.base import engine
from sqlalchemy import update
from sqlalchemy.orm import Session
from app.models.mentee import Mentee

def create_mentee(user, mentee_data):
    if user.role != 'Mentee':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized profile')
    with Session(engine) as session:
        new_mentee = Mentee(
            user_id = mentee_data.user_id,
            goals= mentee_data.goals,
            preferred_skills= mentee_data.preferred_skills
        )
        session.add(new_mentee)
        session.commit()
        
        return new_mentee
    
def update_mentee(user, update_info):
    with Session(engine) as session:
        update_data = update_info.dict(exclude_unset=True, exclude_none=True)

        if not update_data:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid update request')
        
        stmt = (
            update(Mentee)
            .where(Mentee.user_id == user.id)
            .values(**update_data)
            .returning(Mentee)
        )

        result = session.execute(stmt)
        updated_mentee = result.scalar_one_or_none()

        if not updated_mentee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Mentee profile not found')
        
        return updated_mentee