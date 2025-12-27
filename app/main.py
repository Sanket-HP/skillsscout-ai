from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.routes import users, projects, companies


# --------------------------------------------------
# App initialization
# --------------------------------------------------
app = FastAPI(
    title="SkillScout AI Backend",
    description="Backend APIs for SkillScout AI (Skill-first hiring platform)",
    version="1.0.0"
)

# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------
# Allow frontend HTML pages to call backend APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Register API Routes
# --------------------------------------------------
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(companies.router, prefix="/companies", tags=["Companies"])

# --------------------------------------------------
# Health Check (Render needs this)
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "running",
        "service": "SkillScout AI Backend",
        "message": "Backend is live and healthy 🚀"
    }

@app.get("/health")
def health_check():
    return {"ok": True}
