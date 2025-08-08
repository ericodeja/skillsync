from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, ARRAY
from typing import Optional

class Mentee(Base):
    __tablename__ = 'mentees'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    goals: Mapped[Optional[str]]
    preferred_skills: Mapped[list[str]] = mapped_column(ARRAY(String))