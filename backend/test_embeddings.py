import numpy as np

embeddings = np.load("embeddings/embeddings.npy")
image_ids = np.load("embeddings/image_ids.npy")

print("=" * 50)

print("Embedding Shape")

print(embeddings.shape)

print()

print("Image IDs Shape")

print(image_ids.shape)

print()

print("First Image")

print(image_ids[0])

print()

print("Embedding Dimension")

print(len(embeddings[0]))