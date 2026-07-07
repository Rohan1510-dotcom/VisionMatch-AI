from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_service import save_uploaded_file

router = APIRouter()


ALLOWED_TYPES = [
    "image/jpeg",
    "image/png",
    "image/jpg"
]

MAX_FILE_SIZE = 5 * 1024 * 1024


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_TYPES:

        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG images are allowed."
        )

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:

        raise HTTPException(
            status_code=400,
            detail="Image size exceeds 5 MB."
        )

    file.file.seek(0)

    filename, path = save_uploaded_file(file)

    return {

        "success": True,

        "message": "Image uploaded successfully!",

        "filename": filename,

        "content_type": file.content_type,

        "file_size": len(contents),

        "path": path

    }