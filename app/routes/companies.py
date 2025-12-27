from fastapi import APIRouter, Depends
from app.core.auth_middleware import firebase_auth
from app.core.firebase import db


router = APIRouter(tags=["Companies"])


@router.get("/candidates")
async def discover_candidates(
    _: dict = Depends(firebase_auth)
):
    """
    Get all candidates (basic discovery)
    """
    users_ref = (
        db.collection("users")
        .where("role", "==", "candidate")
        .stream()
    )

    candidates = []
    for user in users_ref:
        data = user.to_dict()
        data["id"] = user.id
        candidates.append(data)

    return candidates


@router.get("/candidate/{candidate_id}/projects")
async def view_candidate_projects(
    candidate_id: str,
    _: dict = Depends(firebase_auth)
):
    """
    View projects of a specific candidate
    """
    projects_ref = (
        db.collection("projects")
        .where("ownerId", "==", candidate_id)
        .stream()
    )

    projects = []
    for project in projects_ref:
        data = project.to_dict()
        data["id"] = project.id
        projects.append(data)

    return projects
