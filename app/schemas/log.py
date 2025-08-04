from pydantic import BaseModel, EmailStr

class Log(BaseModel):
    email: EmailStr
    password: str