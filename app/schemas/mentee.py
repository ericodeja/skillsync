from pydantic import BaseModel
from typing import Optional

class Mentee(BaseModel):
    user_id: int
    goals: Optional[str]
    preferred_skills: list

class MenteeUpdate(BaseModel):
    goals: Optional[str]
    preferred_skills: Optional[list]