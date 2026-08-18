import pandas as pd
import os

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
csv_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "DataCoSupplyChainDataset.csv"
)

df = pd.read_csv(csv_path, encoding="latin1")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# -----------------------------
# 2. BASIC INFORMATION
# -----------------------------
print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# -----------------------------
# 3. DATA TYPES
# -----------------------------
print("\n===== DATA TYPES =====")
print(df.dtypes)

# -----------------------------
# 4. STATISTICAL SUMMARY
# -----------------------------
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# -----------------------------
# 5. SALES ANALYSIS
# -----------------------------
print("\n===== SALES ANALYSIS =====")

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
maximum_sales = df["Sales"].max()
minimum_sales = df["Sales"].min()

print("Total Sales:", round(total_sales, 2))
print("Average Sales:", round(average_sales, 2))
print("Maximum Sales:", round(maximum_sales, 2))
print("Minimum Sales:", round(minimum_sales, 2))

# -----------------------------
# 6. PROFIT ANALYSIS
# -----------------------------
print("\n===== PROFIT ANALYSIS =====")

total_profit = df["Order Profit Per Order"].sum()
average_profit = df["Order Profit Per Order"].mean()

print("Total Profit:", round(total_profit, 2))
print("Average Profit per Order:", round(average_profit, 2))

# -----------------------------
# 7. ORDER ANALYSIS
# -----------------------------
print("\n===== ORDER ANALYSIS =====")

print("Unique Orders:", df["Order Id"].nunique())
print("Unique Customers:", df["Customer Id"].nunique())

# -----------------------------
# 8. CATEGORY ANALYSIS
# -----------------------------
print("\n===== TOP 10 CATEGORIES BY SALES =====")

category_sales = (
    df.groupby("Category Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(category_sales)

# -----------------------------
# 9. MARKET ANALYSIS
# -----------------------------
print("\n===== SALES BY MARKET =====")

market_sales = (
    df.groupby("Market")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(market_sales)

# -----------------------------
# 10. SHIPPING MODE ANALYSIS
# -----------------------------
print("\n===== SHIPPING MODE ANALYSIS =====")

shipping_analysis = df.groupby("Shipping Mode").agg(
    Sales=("Sales", "sum"),
    Profit=("Order Profit Per Order", "sum"),
    Late_Delivery_Risk=("Late_delivery_risk", "mean")
)

shipping_analysis["Late_Delivery_Risk"] *= 100

print(shipping_analysis.sort_values(
    "Late_Delivery_Risk",
    ascending=False
))

# -----------------------------
# 11. DELIVERY STATUS
# -----------------------------
print("\n===== DELIVERY STATUS =====")

print(df["Delivery Status"].value_counts())

# -----------------------------
# 12. CUSTOMER SEGMENT
# -----------------------------
print("\n===== CUSTOMER SEGMENT ANALYSIS =====")

customer_segment = (
    df.groupby("Customer Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print(customer_segment)

# -----------------------------
# 13. LATE DELIVERY RISK
# -----------------------------
print("\n===== OVERALL LATE DELIVERY RISK =====")

late_risk = df["Late_delivery_risk"].mean() * 100

print("Late Delivery Risk:", round(late_risk, 2), "%")

# -----------------------------
# 14. DATE ANALYSIS
# -----------------------------
df["order_date"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

df["Year"] = df["order_date"].dt.year
df["Month"] = df["order_date"].dt.month

monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

print("\n===== ANALYSIS COMPLETED SUCCESSFULLY =====")