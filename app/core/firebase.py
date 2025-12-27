import firebase_admin
from firebase_admin import credentials, auth, firestore
from app.core.config import SERVICE_ACCOUNT_PATH, FIREBASE_PROJECT_ID

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred, {
        "projectId": FIREBASE_PROJECT_ID
    })

# Firestore client
db = firestore.client()


def verify_firebase_token(token: str):
    """
    Verify Firebase ID token from frontend
    """
    decoded_token = auth.verify_id_token(token)
    return decoded_token
