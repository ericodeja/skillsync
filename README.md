# SkillSync

**SkillSync** is a real-time micro-mentorship platform that matches learners with experts for short, high-impact guidance sessions. Designed for speed, clarity, and scale.

---

## Vision

Enable anyone, anywhere to get unstuck instantly by syncing with the right mentor — in seconds, not days.

---

##  Tech Stack

- **FastAPI** – high-performance async Python backend  
- **PostgreSQL** – relational database  
- **SQLAlchemy** – async ORM for database models  
- **JWT Auth** – secure access with scope-based control  
- **Redis** *(planned)* – fast in-memory storage for sessions and matching  
- **Celery** *(planned)* – background job processing  
- **WebSockets** *(planned)* – real-time notifications and sync  

---

## Local Setup

> Requirements: Python 3.11+, PostgreSQL, virtualenv

```bash
# Clone the repo
git clone https://github.com/ericodeja/skillsync.git
cd skillsync

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
````

---

## Progress Tracker

* [x] Initialize FastAPI project
* [x] Connect PostgreSQL with SQLAlchemy
* [x] Create User model + CRUD operations
* [x] Implement JWT Authentication
* [x] Role & Scope-based access control
* [ ] Session booking system (MVP)
* [ ] Smart matching algorithm
* [ ] Real-time mentorship via WebSockets
* [ ] Background jobs with Celery
* [ ] Rate-limiting & abuse prevention

---

## Folder Structure

```
skillsync/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── crud/
│   └── core/
├── requirements.txt
├── README.md
└── LICENSE
```

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

## Status

Actively being built. MVP in progress.
Feedback, suggestions, and collaboration are welcome.

