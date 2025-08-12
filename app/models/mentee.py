from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, ARRAY
from typing import Optional


class Mentee(Base):
    __tablename__ = 'mentees'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    goals: Mapped[Optional[str]]
    preferred_skills: Mapped[list[str]] = mapped_column(ARRAY(String))

    user: Mapped['User'] = relationship(back_populates='mentee_profile') # type: ignore
