import os
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# Application Config
# --------------------------------------------------

PROJECT_NAME = "SkillScout AI Backend"

# Firebase project ID (still useful for reference/logs)
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "skillscout-ai-514ff")
