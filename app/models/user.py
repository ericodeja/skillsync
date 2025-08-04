from sqlalchemy import String, Date, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.db.base import Base, engine
from datetime import datetime



class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(150))
    gender: Mapped[str] = mapped_column(String(7))
    date_of_birth: Mapped[datetime] = mapped_column(Date)
    country: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(default=True)
    password: Mapped[str]




