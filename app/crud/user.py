from app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.base import engine
from app.schemas.user import UserBase
from app.core.security import hash_password


def create_user(user_data):
    with Session(engine) as session:
        new_user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            gender=user_data.gender,
            date_of_birth=user_data.date_of_birth,
            country=user_data.country,
            password=hash_password(user_data.password)
        )

        if new_user.role == "mentor" and new_user.mentee_profile:
            raise ValueError("User cannot be both mentor and mentee")
        if new_user.role == "mentee" and new_user.mentor_profile:
            raise ValueError("User cannot be both mentor and mentee")
        
        session.add(new_user)
        session.commit()
        return UserBase(id=new_user.id, username=new_user.first_name)


def delete_user(user):
    with Session(engine) as session:
        stmt = select(User).where(User.id == user.id)
        result = session.execute(stmt).scalar_one_or_none()

        session.delete(result)
        session.commit()
