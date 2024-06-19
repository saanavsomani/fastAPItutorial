from fastapi import FastAPI

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


