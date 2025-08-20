from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class UserBase(BaseModel):
    id: int
    username: str
    role: str

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    gender: str
    date_of_birth: date
    country: str
    password:str
    role: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    gender: Optional[str] = None
    
