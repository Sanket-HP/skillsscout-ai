from fastapi import APIRouter, Request, Depends, HTTPException
from app.core.auth_middleware import firebase_auth
from app.core.firebase import db


router = APIRouter(tags=["Users"])


@router.get("/me")
async def get_my_profile(
    request: Request,
    _: dict = Depends(firebase_auth)
):
    """
    Get logged-in user's profile
    """
    uid = request.state.user["uid"]
    doc = db.collection("users").document(uid).get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="User profile not found")

    return doc.to_dict()


@router.post("/update")
async def update_my_profile(
    data: dict,
    request: Request,
    _: dict = Depends(firebase_auth)
):
    """
    Update logged-in user's profile
    """
    uid = request.state.user["uid"]

    db.collection("users").document(uid).set(data, merge=True)

    return {
        "status": "success",
        "message": "Profile updated successfully"
    }
