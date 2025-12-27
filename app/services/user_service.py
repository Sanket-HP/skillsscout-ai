from app.core.firebase import db
from fastapi import HTTPException


def get_user_by_id(user_id: str):
    doc = db.collection("users").document(user_id).get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")

    data = doc.to_dict()
    data["id"] = user_id
    return data


def update_user_profile(user_id: str, data: dict):
    db.collection("users").document(user_id).set(data, merge=True)

    return {
        "status": "success",
        "message": "User profile updated"
    }
