import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "sample_dataset.csv"

def load_dataset():
    print("=" * 60)
    print("CREWAI - SAMPLE DATA LOADER")
    print("=" * 60)
    df = pd.read_csv(DATA_PATH)
    print("\nDataset loaded successfully!")
    print("\n=== Dataset Information ===")
    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])
    print("\n=== Column Names ===")
    print(df.columns.tolist())
    print("\n=== Data Types ===")
    print(df.dtypes)
    print("\n=== First 5 Rows ===")
    print(df.head(5).to_string(index=False))
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    print("\nDuplicate records:", df.duplicated().sum())
    print("\n=== Task Priority Distribution ===")
    print(df["priority"].value_counts())
    print("\nDataset ready for multi-agent processing.")
    return df

if __name__ == "__main__":
    load_dataset()
