from app.core.firebase import db


def get_all_candidates():
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


def get_candidate_projects(candidate_id: str):
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
