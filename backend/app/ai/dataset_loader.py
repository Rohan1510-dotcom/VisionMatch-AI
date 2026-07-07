import pandas as pd

DATASET_PATH = "dataset/styles.csv"

def load_dataset():
    df = pd.read_csv(
        DATASET_PATH,
        on_bad_lines="skip"
    )

    return df