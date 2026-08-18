import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================
# LOAD DATASET
# ==============================

csv_path = r"C:\Users\sanka\OneDrive\Desktop\project\data\DataCoSupplyChainDataset.csv"

df = pd.read_csv(csv_path, encoding="latin1")

# ==============================
# CREATE VISUALIZATION FOLDER
# ==============================

charts_folder = r"C:\Users\sanka\OneDrive\Desktop\project\visualizations"

os.makedirs(charts_folder, exist_ok=True)

print("Dataset loaded!")
print("Creating charts...")


# ==============================
# 1. SALES BY MARKET
# ==============================

market_sales = (
    df.groupby("Market")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))
market_sales.plot(kind="bar")
plt.title("Sales by Market")
plt.xlabel("Market")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(charts_folder, "sales_by_market.png")
)

plt.close()

print("1. Sales by Market - DONE")


# ==============================
# 2. TOP 10 CATEGORIES
# ==============================

category_sales = (
    df.groupby("Category Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
category_sales.sort_values().plot(kind="barh")
plt.title("Top 10 Product Categories by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig(
    os.path.join(charts_folder, "top_10_categories.png")
)

plt.close()

print("2. Top 10 Categories - DONE")


# ==============================
# 3. SHIPPING MODE RISK
# ==============================

shipping_risk = (
    df.groupby("Shipping Mode")["Late_delivery_risk"]
    .mean() * 100
)

plt.figure(figsize=(9, 5))
shipping_risk.plot(kind="bar")
plt.title("Late Delivery Risk by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Late Delivery Risk (%)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(charts_folder, "shipping_mode_risk.png")
)

plt.close()

print("3. Shipping Mode Risk - DONE")


# ==============================
# 4. CUSTOMER SEGMENT SALES
# ==============================

segment_sales = (
    df.groupby("Customer Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")
plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(charts_folder, "customer_segment_sales.png")
)

plt.close()

print("4. Customer Segment Sales - DONE")


# ==============================
# 5. MONTHLY SALES TREND
# ==============================

df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

monthly_sales = (
    df.groupby(
        df["order date (DateOrders)"].dt.to_period("M")
    )["Sales"]
    .sum()
)

plt.figure(figsize=(12, 5))
plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=60)
plt.tight_layout()

plt.savefig(
    os.path.join(charts_folder, "monthly_sales_trend.png")
)

plt.close()

print("5. Monthly Sales Trend - DONE")


# ==============================
# FINAL
# ==============================

print("\n===================================")
print(" ALL 5 CHARTS CREATED SUCCESSFULLY ")
print("===================================")

print("\nSaved in:")
print(charts_folder)