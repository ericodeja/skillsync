from app.models.user import User
from sqlalchemy.orm import Session
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
        session.add(new_user)
        session.commit()
        return UserBase(id=new_user.id, username=new_user.first_name)
    
