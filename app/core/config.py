import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "SkillScout AI Backend"

FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "skillscout-ai-514ff")

SERVICE_ACCOUNT_PATH = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS",
    "firebase-service-account.json"
)
