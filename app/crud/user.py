from fastapi import HTTPException, status
from app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from app.db.base import engine
from app.schemas.user import UserBase
from app.core.security import hash_password


def create_user(user_data):
    with Session(engine) as session:
        if user_data.role != "Mentor" or user_data.role != "Mentee":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid user role')
        new_user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            gender=user_data.gender,
            date_of_birth=user_data.date_of_birth,
            country=user_data.country,
            password=hash_password(user_data.password),
            role=user_data.role
        )

        if new_user.role == "Mentor" and new_user.mentee_profile:
            raise ValueError("User cannot be both mentor and mentee")
        if new_user.role == "Mentee" and new_user.mentor_profile:
            raise ValueError("User cannot be both mentor and mentee")

        session.add(new_user)
        session.commit()
        return UserBase(id=new_user.id, username=new_user.first_name)


def update_user(user, update_info):
    with Session(engine) as session:
        update_data = update_info.dict(exclude_unset=True, exclude_none=True)

        if not update_data:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='No valid fields provided for update')

        stmt = (update(User)
                .where(User.id == user.id)
                .values(**update_data)
                .returning(User)
                )

        result = session.execute(stmt)
        updated_user = result.scalar_one_or_none()

        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User doen't exist")

        session.commit()

        return updated_user


def delete_user(user):
    with Session(engine) as session:
        stmt = select(User).where(User.id == user.id)
        result = session.execute(stmt).scalar_one_or_none()

        session.delete(result)
        session.commit()
