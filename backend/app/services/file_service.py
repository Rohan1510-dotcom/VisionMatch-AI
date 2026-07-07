import os
import shutil
import uuid


UPLOAD_FOLDER = "app/uploads"


def save_uploaded_file(file):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    return unique_filename, file_path