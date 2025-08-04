from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings



if settings.DATABASE_URL is None:
    raise ValueError('DATABASE_URL is not set in the .env file')
engine = create_engine(settings.DATABASE_URL)


class ReprMixin:
    def __repr__(self):
        cls = self.__class__.__name__
        fields = ', '.join(
            f"{key}={getattr(self, key)!r}"
            for key in self.__dict__.keys()
            if not key.startswith('_')
        )
        return f"{cls}({fields})"


class Base(DeclarativeBase, ReprMixin):
    pass


