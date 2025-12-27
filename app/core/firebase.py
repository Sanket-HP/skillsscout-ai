import os
import json
import firebase_admin
from firebase_admin import credentials, auth, firestore

# --------------------------------------------------
# Load Firebase credentials from ENV (Render-safe)
# --------------------------------------------------

service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

if not service_account_json:
    raise RuntimeError("FIREBASE_SERVICE_ACCOUNT environment variable is not set")

service_account_info = json.loads(service_account_json)

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()


def verify_firebase_token(token: str):
    """
    Verify Firebase ID token from frontend
    """
    return auth.verify_id_token(token)
