from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/", description = "This is our base route when our app opens.")
async def base_get_root():
  return {"message": "Welcome to my practice fastAPI application!"}

@app.post("/")
async def post():
  return {"message": "Welcome to post!"}

@app.put("/")
async def put():
  return {"message": "Welcome to put!"}

@app.get("/users")
async def list_users():
  return {"message": "List of users"}

#  want this specific endpoint first before the dynamic endpoint
#  (order of routes matter)
@app.get("users/current_user")
async def get_current_user():
  return {"message":"This is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
  return {"user_id": user_id}

class SportEnum(str, Enum):
  basketball = "basketball"
  football = "football"
  baseball = "baseball"

@app.get("/sports/{sport}")
async def get_sport(sport: SportEnum):
  if sport == SportEnum.basketball:
    return {"sport": sport, "GOAT": "Michael Jordan"}
  elif sport == SportEnum.football: # can check value - sport == "football"
    return {"sport": sport, "GOAT": "Tom Brady"}
  return {"sport": sport, "GOAT": "Babe Ruth"}