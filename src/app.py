"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {

    "Basketball Team": {
        "description": "Join the basketball team and compete in local tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu", "lucas@mergington.edu"]
    },
    "Soccer Club": {
        "description": "Practice soccer skills and participate in matches",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Explore various art techniques and create your own masterpieces",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["amelia@mergington.edu", "isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Learn acting skills and perform in school plays",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["mia@mergington.edu", "harper@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging problems and prepare for math competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 25,
        "participants": ["elijah@mergington.edu", "logan@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "p"
        "articipants": ["charlotte@mergington.edu", "ava@mergington.edu"]
    },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")
    
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

    
