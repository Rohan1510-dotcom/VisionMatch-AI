import os

from app.ai.dataset_loader import load_dataset

IMAGE_FOLDER = "dataset/images"

df = load_dataset()

missing = 0

for image_id in df["id"]:

    image_path = os.path.join(
        IMAGE_FOLDER,
        f"{image_id}.jpg"
    )

    if not os.path.exists(image_path):
        missing += 1

print(f"Missing Images : {missing}")
print(f"Available Images : {len(df) - missing}")