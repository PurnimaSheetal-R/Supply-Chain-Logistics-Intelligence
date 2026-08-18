import pandas as pd

csv_path = r"C:\Users\sanka\OneDrive\Desktop\project\data\DataCoSupplyChainDataset.csv"

df = pd.read_csv(csv_path, encoding="latin1")

print("Dataset loaded successfully!")
print("Original Shape:", df.shape)

print("Dataset loaded successfully!")
print("Original Shape:", df.shape)

# -----------------------------
# STEP 2: DATA CLEANING
# -----------------------------

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Convert date columns
df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

df["shipping date (DateOrders)"] = pd.to_datetime(
    df["shipping date (DateOrders)"],
    errors="coerce"
)

# Fill missing values
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")
df["Customer Zipcode"] = df["Customer Zipcode"].fillna(0)
df["Order Zipcode"] = df["Order Zipcode"].fillna(0)

# Remove duplicate rows
df = df.drop_duplicates()

print("\n===== STEP 2: CLEANING RESULTS =====")
print("Shape after cleaning:", df.shape)
print("Duplicate rows:", df.duplicated().sum())

print("\nRemaining missing values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\n===== STEP 2 COMPLETED =====")