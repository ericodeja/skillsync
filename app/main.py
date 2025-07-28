from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return 'Welcome to skillsync.' \
        ' A real-time micro-mentorship platform that matches learners with experts for short, high-impact guidance sessions. Designed for speed, clarity, and scale.'
