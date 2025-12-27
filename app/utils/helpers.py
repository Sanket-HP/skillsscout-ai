from datetime import datetime
from fastapi import HTTPException


def current_utc_time():
    """
    Returns current UTC time
    """
    return datetime.utcnow()


def success_response(message: str, data=None):
    """
    Standard success response format
    """
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def error_response(message: str, status_code: int = 400):
    """
    Standard error response helper
    """
    raise HTTPException(status_code=status_code, detail=message)


def sanitize_dict(data: dict, allowed_fields: list):
    """
    Remove unwanted keys from input data
    """
    return {k: v for k, v in data.items() if k in allowed_fields}


def paginate_list(items: list, page: int = 1, limit: int = 10):
    """
    Simple pagination helper
    """
    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(items),
        "results": items[start:end]
    }


def is_candidate(user_data: dict):
    """
    Check if user role is candidate
    """
    return user_data.get("role") == "candidate"


def is_company(user_data: dict):
    """
    Check if user role is company
    """
    return user_data.get("role") == "company"
