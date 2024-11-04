from google.cloud import firestore
from config import db

# Add a new user to Firestore
def create_user(user_data):
    user_ref = db.collection("users").document()
    user_ref.set(user_data)
    return user_ref.id

# Retrieve user details
def get_users():
    users = []
    for user in db.collection("users").stream():
        users.append(user.to_dict())
    return users

# Update user details
def update_user(user_id, user_data):
    user_ref = db.collection("users").document(user_id)
    user_ref.update(user_data)
    return user_ref.get().to_dict()

# Delete user
def delete_user(user_id):
    db.collection("users").document(user_id).delete()
    return {"status": "deleted"}
