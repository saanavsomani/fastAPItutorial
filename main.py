from fastapi import FastAPI
from enum import Enum
# from typing import Optional
from pydantic import BaseModel

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
async def get_user(user_id: int):
  return {"user_id": user_id}

class SportEnum(str, Enum):
  basketball = "basketball"
  football = "football"
  baseball = "baseball"

@app.get("/sports/get/{sport}")
async def get_sport(sport: SportEnum):
  if sport == SportEnum.basketball:
    return {"sport": sport, "GOAT": "Michael Jordan"}
  elif sport == SportEnum.football: # can check value - sport == "football"
    return {"sport": sport, "GOAT": "Tom Brady"}
  return {"sport": sport, "GOAT": "Babe Ruth"}


fake_sports_db = [{"sport" : "basektball"}, {"sport" : "football"}, {"sport" : "baseball"}]
# intro to query parameters
@app.get("/sports")
async def list_sports(skip: int = 0, limit: int = 10):
  return fake_sports_db[skip: skip + limit]

# allows for optional query parameters - q: Optional[str] = None
# using pydantic type conversion
# Ex: http://localhost:8000/sports/optional/basketball?q=dribbling&short=no
# same as http://localhost:8000/sports/optional/basketball?q=dribbling&short=0
@app.get("/sports/optional/{sport}")
async def get_sport_optional(sport: str, q: str | None = None, short: bool = False):
  sport = {"sport" : sport}
  if q:
    sport.update({"q" : q})
  if not short:
    sport.update({"description" : "Sports update"})
  return sport

@app.get("/users/{user_id}/sports/{sport}")
async def get_user_sport(user_id: int, sport: str, q: str | None = None, short: bool = False):
  user_sport = {"user_id" : user_id, "sport" : sport}
  if q:
    user_sport.update({"q" : q})
  if not short:
    user_sport.update({"description" : f"{user_id} likes {sport}"})
  return user_sport


class SportType(BaseModel):
  name: str
  GOAT: str
  description: str | None = None

# using Request Body
@app.post("/sports/create")
async def create_sport(sport: SportType) -> SportType:
  sport_dict = sport.model_dump(); # dictionary that stores sports
  if sport.description:
    sport_dict.update({"description" : sport.description})
  return sport_dict

@app.put("/sports/create/{sport_id}")
async def create_sport_put(sport_id: int, sport: SportType, q: str | None = None):
    result = {"item_id": sport_id, **sport.model_dump()}
    if q:
        result.update({"q": q})
    return result