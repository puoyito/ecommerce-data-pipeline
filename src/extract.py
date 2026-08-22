import pandas as pd
from pathlib import Path


def extract_data(file_path: str | Path) -> pd.DataFrame:
    """
    Extract data from a CSV file.
    """
    
    print(f"Reading data from: {file_path}")

    df = pd.read_csv(file_path, encoding='unicode_escape')
    #df = pd.DataFrame()
    print(f"Records extracted: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    return df


if __name__ == "__main__":
    file_path = Path("./data/raw/data.csv")

    if not file_path.is_file():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    print(f"File path: {file_path}")
    df = extract_data(file_path)

    print("\nFirst 5 records:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate records:")
    print(df.duplicated().sum())