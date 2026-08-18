import sqlite3
import pandas as pd
import os

# CSV location
csv_path = r"C:\Users\sanka\OneDrive\Desktop\project\data\DataCoSupplyChainDataset.csv"

# Database location
db_path = r"C:\Users\sanka\OneDrive\Desktop\project\data\supply_chain.db"

# Load CSV
df = pd.read_csv(csv_path, encoding="latin1")

# Connect to SQLite
conn = sqlite3.connect(db_path)

# Create table
df.to_sql(
    "supply_chain",
    conn,
    if_exists="replace",
    index=False
)

print("CSV loaded into SQLite successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

conn.close()