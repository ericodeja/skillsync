from pydantic import BaseModel
from typing import Optional, List


class Mentor(BaseModel):
    user_id: int
    bio: Optional[str]
    years_of_experience: int
    timezone: str
    available_hours: Optional[dict]
    skills: List[str]
    rating: float
    