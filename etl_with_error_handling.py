import pandas as pd
import sqlite3
import os

source_csv = "people.csv"
file_path = r"C:\Users\Prashil Singh\PycharmProjects\etl_project\people.csv"

def extract(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Source file not found: {file_path}")
        df = pd.read_csv(file_path)
        print(" Extraction successful")
        return df
    except Exception as e:
        print(f" Extraction error: {e}")
        return None


def transform(df):
    try:
        if df is None or df.empty:
            raise ValueError("No data to transform")
        
        # Example transformation: fill missing values and convert columns
        df['age'] = df['age'].fillna(0).astype(int)
        df['name'] = df['name'].fillna("Unknown").str.title()
        
        print(" Transformation successful")
        return df
    except Exception as e:
        print(f" Transformation error: {e}")
        return None


def load(df, db_file, table_name="people"):
    try:
        if df is None or df.empty:
            raise ValueError("No data to load")
        
        conn = sqlite3.connect(db_file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print(" Loading successful")
    except Exception as e:
        print(f" Loading error: {e}")


if __name__ == "__main__":
    # Example ETL run
    source_csv = "people.csv"   # make sure this file exists
    target_db = "etl_example.db"
    
    # Run ETL
    data = extract(source_csv)
    transformed = transform(data)
    load(transformed, target_db)
