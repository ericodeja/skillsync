from app.db.base import engine
from sqlalchemy.orm import Session
from app.models.mentors import Mentor


def create_mentor(mentor_data):
    with Session(engine) as session:
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