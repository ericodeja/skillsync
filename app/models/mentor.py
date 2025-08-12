from app.db.base import Base
from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from typing import Optional


class Mentor(Base):
    __tablename__ = 'mentors'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    bio: Mapped[Optional[str]]
    years_of_experience: Mapped[int]
    timezone: Mapped[str]
    available_hours: Mapped[Optional[dict]] = mapped_column(JSONB, default=dict)
    skills: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    rating: Mapped[float] = mapped_column(Numeric(3,2), default=0.0)
    session_count: Mapped[int] = mapped_column(default=0)
    is_verified: Mapped[bool] = mapped_column(default=False)

    user: Mapped['User'] = relationship(back_populates='mentor_profile') # type: ignore
