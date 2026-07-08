import torch
import clip

# Automatically choose GPU if available, otherwise CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load CLIP model
model, preprocess = clip.load("ViT-B/32", device=device)

print("=" * 50)
print("CLIP Model Loaded Successfully!")
print("=" * 50)
print(f"Device : {device}")
print(f"Model  : ViT-B/32")