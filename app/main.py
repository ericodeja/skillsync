from fastapi import FastAPI, Security
from app.api.v1.routes_user import router as user_routes
from app.api.v1.routes_log import router as log_routes
from app.api.v1.routes_token import router as token_routes
from app.schemas.user import UserBase
from app.auth.auth import get_current_user





app = FastAPI()
app.include_router(user_routes, prefix='/users', tags=['Users'])
app.include_router(log_routes, prefix='/auth', tags=['Auth'])
app.include_router(token_routes, prefix='/auth', tags=['Auth'])


@app.get('/')
def index(user: UserBase = Security(get_current_user, scopes=["read: profile"])):
    message = f"{user.username}, Welcome to skillsync.' \
        ' A real-time micro-mentorship platform that matches learners with experts for short, high-impact guidance sessions. Designed for speed, clarity, and scale."
    return message
