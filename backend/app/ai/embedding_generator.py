import os
import numpy as np
import torch
import clip

from PIL import Image
from tqdm import tqdm

# -----------------------------
# Configuration
# -----------------------------

IMAGE_FOLDER = "dataset/images"
EMBEDDING_FOLDER = "embeddings"

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")

model, preprocess = clip.load("ViT-B/32", device=device)

# -----------------------------
# Storage
# -----------------------------

embeddings = []
image_ids = []

# -----------------------------
# Read Images
# -----------------------------

image_files = [
    file
    for file in os.listdir(IMAGE_FOLDER)
    if file.endswith(".jpg")
]

print(f"\nFound {len(image_files)} images\n")

# -----------------------------
# Generate Embeddings
# -----------------------------

for image_name in tqdm(image_files):

    image_path = os.path.join(
        IMAGE_FOLDER,
        image_name
    )

    image = Image.open(image_path).convert("RGB")

    image = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():

        embedding = model.encode_image(image)

    embedding = embedding.cpu().numpy()[0]

    embeddings.append(embedding)

    image_ids.append(image_name)

# -----------------------------
# Save
# -----------------------------

os.makedirs(
    EMBEDDING_FOLDER,
    exist_ok=True
)

np.save(
    os.path.join(
        EMBEDDING_FOLDER,
        "embeddings.npy"
    ),
    np.array(embeddings)
)

np.save(
    os.path.join(
        EMBEDDING_FOLDER,
        "image_ids.npy"
    ),
    np.array(image_ids)
)

print("\nEmbeddings Saved Successfully!")
print(f"Total Embeddings: {len(embeddings)}")