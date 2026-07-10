import os
import faiss
import numpy as np

# -----------------------------
# Paths
# -----------------------------

EMBEDDINGS_PATH = "embeddings/embeddings.npy"
INDEX_PATH = "embeddings/faiss_index.index"


def build_faiss_index():

    print("Loading embeddings...")

    embeddings = np.load(EMBEDDINGS_PATH).astype("float32")

    print(f"Embeddings Shape: {embeddings.shape}")

    # Normalize embeddings
    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    print(f"Embedding Dimension: {dimension}")

    # Create FAISS index
    index = faiss.IndexFlatIP(dimension)

    # Add embeddings
    index.add(embeddings)

    print(f"Indexed {index.ntotal} vectors")

    # Save index
    faiss.write_index(index, INDEX_PATH)

    print("FAISS Index Saved Successfully!")


if __name__ == "__main__":
    build_faiss_index()