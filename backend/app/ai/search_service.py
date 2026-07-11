from app.data.metadata_service import get_metadata
import faiss
import numpy as np
import torch
import clip

from PIL import Image

# -----------------------------
# Configuration
# -----------------------------

device = "cuda" if torch.cuda.is_available() else "cpu"

model, preprocess = clip.load("ViT-B/32", device=device)

INDEX = faiss.read_index("embeddings/faiss_index.index")

IMAGE_IDS = np.load("embeddings/image_ids.npy")

# -----------------------------
# Search Function
# -----------------------------

def search_similar(image_path, top_k=5):

    image = Image.open(image_path).convert("RGB")

    image = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():

        embedding = model.encode_image(image)

    embedding = embedding.cpu().numpy().astype("float32")

    faiss.normalize_L2(embedding)

    distances, indices = INDEX.search(embedding, top_k)

    results = []

    for index, score in zip(indices[0], distances[0]):

        image_name = str(IMAGE_IDS[index])

        metadata = get_metadata(image_name)

        if metadata is None:
            continue

        metadata["image_url"] = f"http://127.0.0.1:8000/images/{image_name}"

        metadata["similarity"] = round(float(score) * 100, 2)

        results.append(metadata)

    return results