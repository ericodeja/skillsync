from fastapi import FastAPI
from app.api.v1.routes_user import router as user_routes




app = FastAPI()
app.include_router(user_routes, prefix='/users', tags=['Users'])


@app.get('/')
async def index():
    return 'Welcome to skillsync.' \
        ' A real-time micro-mentorship platform that matches learners with experts for short, high-impact guidance sessions. Designed for speed, clarity, and scale.'
