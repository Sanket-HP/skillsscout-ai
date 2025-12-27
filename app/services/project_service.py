from app.core.firebase import db
from datetime import datetime
from fastapi import HTTPException


def create_project(owner_id: str, data: dict):
    project = {
        "ownerId": owner_id,
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
        "message": "Project created"
    }


def get_projects_by_owner(owner_id: str):
    projects_ref = (
        db.collection("projects")
        .where("ownerId", "==", owner_id)
        .stream()
    )

    projects = []
    for project in projects_ref:
        data = project.to_dict()
        data["id"] = project.id
        projects.append(data)

    return projects


def get_project_by_id(project_id: str, owner_id: str):
    doc = db.collection("projects").document(project_id).get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Project not found")

    project = doc.to_dict()

    if project["ownerId"] != owner_id:
        raise HTTPException(status_code=403, detail="Unauthorized access")

    project["id"] = project_id
    return project


def update_project(project_id: str, owner_id: str, data: dict):
    doc_ref = db.collection("projects").document(project_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Project not found")

    if doc.to_dict()["ownerId"] != owner_id:
        raise HTTPException(status_code=403, detail="Unauthorized access")

    data["updatedAt"] = datetime.utcnow()
    doc_ref.set(data, merge=True)

    return {
        "status": "success",
        "message": "Project updated"
    }
