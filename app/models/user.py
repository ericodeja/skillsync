from sqlalchemy import String, Date, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.db.base import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(150), unique=True)
    gender: Mapped[str] = mapped_column(String(7))
    date_of_birth: Mapped[datetime] = mapped_column(Date)
    country: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(default=True)
    password: Mapped[str]
    role: Mapped[str] = mapped_column(default='Mentee')

    token: Mapped['Token'] = relationship(back_populates='user', uselist=False, cascade='all, delete-orphan') # type: ignore

    mentor_profile: Mapped[Optional['Mentor']] = relationship( # type: ignore
        back_populates='user', uselist=False, cascade='all, delete-orphan')
    
    mentee_profile: Mapped[Optional['Mentee']] = relationship( # type: ignore
        back_populates='user', uselist=False, cascade='all, delete-orphan')


# Create relationship between user and other tables so deleting the user will delete all user information
