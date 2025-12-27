from fastapi import APIRouter, Request, Depends, HTTPException
from app.core.auth_middleware import firebase_auth
from app.core.firebase import db

from datetime import datetime

router = APIRouter(tags=["Projects"])


@router.post("/create")
async def create_project(
    data: dict,
    request: Request,
    _: dict = Depends(firebase_auth)
):
    """
    Create a new project for logged-in candidate
    """
    uid = request.state.user["uid"]

    project = {
        "ownerId": uid,
        "title": data.get("title"),
        "description": data.get("description", ""),
        "techStack": data.get("techStack", []),
        "status": "in-progress",
        "progress": 0,
        "notes": "",
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow()
    }

    db.collection("projects").add(project)

    return {
        "status": "success",
        "message": "Project created successfully"
    }


@router.get("/my")
async def get_my_projects(
    request: Request,
    _: dict = Depends(firebase_auth)
):
    """
    Get all projects of logged-in candidate
    """
    uid = request.state.user["uid"]

    projects_ref = (
        db.collection("projects")
        .where("ownerId", "==", uid)
        .stream()
    )

    projects = []
    for project in projects_ref:
        data = project.to_dict()
        data["id"] = project.id
        projects.append(data)

    return projects


@router.get("/{project_id}")
async def get_project_by_id(
    project_id: str,
    request: Request,
    _: dict = Depends(firebase_auth)
):
    """
    Get single project (project working page)
    """
    uid = request.state.user["uid"]
    doc = db.collection("projects").document(project_id).get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Project not found")

    project = doc.to_dict()

    if project["ownerId"] != uid:
        raise HTTPException(status_code=403, detail="Access denied")

    project["id"] = project_id
    return project


@router.post("/{project_id}/update")
async def update_project(
    project_id: str,
    data: dict,
    request: Request,
    _: dict = Depends(firebase_auth)
):
    """
    Update project progress, notes, status
    """
    uid = request.state.user["uid"]
    doc_ref = db.collection("projects").document(project_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Project not found")

    if doc.to_dict()["ownerId"] != uid:
        raise HTTPException(status_code=403, detail="Access denied")

    data["updatedAt"] = datetime.utcnow()
    doc_ref.set(data, merge=True)

    return {
        "status": "success",
        "message": "Project updated successfully"
    }
