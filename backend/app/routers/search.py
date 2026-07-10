from fastapi import APIRouter, UploadFile, File
import shutil
import uuid
import os

from app.ai.search_service import search_similar

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/search")
async def search(file: UploadFile = File(...)):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(filepath, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    results = search_similar(filepath)

    return {
        "results": results
    }