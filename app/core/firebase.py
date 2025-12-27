import os
import json
import base64
import firebase_admin
from firebase_admin import credentials, auth, firestore

# --------------------------------------------------
# Load Firebase credentials from BASE64 env variable
# --------------------------------------------------

b64_creds = os.getenv("FIREBASE_SERVICE_ACCOUNT_B64")

if not b64_creds:
    raise RuntimeError("FIREBASE_SERVICE_ACCOUNT_B64 environment variable is not set")

service_account_json = base64.b64decode(b64_creds).decode("utf-8")
service_account_info = json.loads(service_account_json)

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()


def verify_firebase_token(token: str):
    return auth.verify_id_token(token)
