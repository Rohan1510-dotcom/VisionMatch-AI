from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import upload
from app.routers import search

# Create FastAPI app
app = FastAPI(
    title="VisionMatch AI API",
    description="Backend API for VisionMatch AI",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(upload.router)
app.include_router(search.router)

# Serve dataset images
app.mount(
    "/images",
    StaticFiles(directory="dataset/images"),
    name="images"
)

@app.get("/")
def root():
    return {
        "message": "VisionMatch AI Backend is Running!"
    }