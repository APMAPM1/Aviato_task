from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firestore_utils import create_user, get_users, update_user, delete_user

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    project_id: int

# Endpoint to create a user
@app.post("/add_users")
async def add_user(user: User):
    user_id = create_user(user.dict())
    return {"user_id": user_id, **user.dict()}

# Endpoint to get all users
@app.get("/get_users")
async def read_users():
    return get_users()

# Endpoint to update a user
@app.patch("/update_users/{user_id}")
async def update_user_details(user_id: str, user: User):
    updated_user = update_user(user_id, user.dict())
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Endpoint to delete a user
@app.delete("/delete_users/{user_id}")
async def delete_user(user_id: str):
    delete_user(user_id)
    return {"status": "User deleted"}

# Send Invite (example)
@app.post("/send_invite")
async def send_invite():
    # Configure email setup here
    recipients = [
        "shraddha@aviato.consulting",
        "pooja@aviato.consulting",
        "prijesh@aviato.consulting",
        "hiring@aviato.consulting"
    ]
    # Your email sending logic goes here
    # Send Redoc link and Firestore screenshot (manually attach this screenshot)
    return {"status": "Invitation sent"}
