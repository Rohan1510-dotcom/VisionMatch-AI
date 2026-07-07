from app.ai.dataset_loader import load_dataset

df = load_dataset()

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(f"Total Products : {len(df)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Products:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())



