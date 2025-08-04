from app.db.base import Base, engine
from app.models import user

Base.metadata.create_all(engine)