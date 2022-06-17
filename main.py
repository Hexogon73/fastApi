from fastapi import FastAPI
from fastapi import Form

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello world"}


@app.get("/users/{user_id}")
async def user(user_id: str):
    return {"user_id": user_id}


users = ["Spike", "Jet", "Ed", "Faye", "Ein"]


@app.get("/users")
async def users_(start: int = 0, limit: int = 10):
    return users[start:start + limit]


@app.post("/lookup")
async def userlookup(username: str = Form(...), user_id: str = Form("")):
    return {"username": username, "user_id": user_id}
