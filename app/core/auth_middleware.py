from fastapi import Request, HTTPException, Depends
from app.core.firebase import verify_firebase_token



async def firebase_auth(request: Request):
    """
    Dependency to verify Firebase auth token
    """
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header format")

    token = auth_header.split(" ")[1]

    try:
        decoded_token = verify_firebase_token(token)
        request.state.user = decoded_token
        return decoded_token
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
