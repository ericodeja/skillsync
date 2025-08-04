from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Token(Base):
    __tablename__ = 'tokens'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str]
    expiry_time: Mapped[int]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))


