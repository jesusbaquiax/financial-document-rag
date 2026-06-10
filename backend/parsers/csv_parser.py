import pandas as pd
from backend.services.categorizer import categorize_transaction

def parse_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df["category"] = df["description"].apply(categorize_transaction)

    return df