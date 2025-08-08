from app.db.base import engine
from sqlalchemy.orm import Session
from app.models.mentee import Mentee

def create_mentee(mentee_data):
    with Session(engine) as session:
        new_mentee = Mentee(
            user_id = mentee_data.user_id,
            goals= mentee_data.goals,
            preferred_skills= mentee_data.preferred_skills
        )
        session.add(new_mentee)
        session.commit()
        
        return new_mentee