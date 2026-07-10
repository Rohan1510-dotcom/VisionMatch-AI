import pandas as pd

DATASET_PATH = "dataset/styles.csv"

# Load once when the application starts
df = pd.read_csv(
    DATASET_PATH,
    encoding="utf-8",
    low_memory=False,
    on_bad_lines="skip"
)

# Convert id column to string for easy comparison
df["id"] = df["id"].astype(str)


def get_metadata(image_name):
    """
    image_name example:
    '1163.jpg'
    """

    image_id = image_name.replace(".jpg", "")

    product = df[df["id"] == image_id]

    if product.empty:
        return None

    product = product.iloc[0]

    return {
        "id": product["id"],
        "product_name": product["productDisplayName"],
        "gender": product["gender"],
        "master_category": product["masterCategory"],
        "sub_category": product["subCategory"],
        "article_type": product["articleType"],
        "color": product["baseColour"],
        "season": product["season"],
        "usage": product["usage"],
    }