from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    id: int
    username: str

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    gender: str
    date_of_birth: date
    country: str
    password:str
    role: str

