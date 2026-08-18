import pandas as pd
import numpy as np

# ==============================
# LOAD DATA
# ==============================

file_path = "data/DataCoSupplyChainDataset.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# ==============================
# PRODUCT DEMAND ANALYSIS
# ==============================

product_demand = (
    df.groupby(["Product Card Id", "Product Name"])
    .agg(
        Total_Quantity=("Order Item Quantity", "sum"),
        Total_Sales=("Sales", "sum"),
        Number_of_Orders=("Order Id", "nunique")
    )
    .reset_index()
)

# Average quantity per order
product_demand["Avg_Quantity_Per_Order"] = (
    product_demand["Total_Quantity"] /
    product_demand["Number_of_Orders"]
)

# Rank products by demand
product_demand["Demand_Rank"] = (
    product_demand["Total_Quantity"]
    .rank(method="dense", ascending=False)
)


# ==============================
# FAST MOVERS
# ==============================

print("\n===================================")
print("TOP 10 FAST-MOVING PRODUCTS")
print("===================================")

fast_movers = product_demand.sort_values(
    "Total_Quantity",
    ascending=False
).head(10)

print(
    fast_movers[
        [
            "Product Name",
            "Total_Quantity",
            "Total_Sales",
            "Number_of_Orders"
        ]
    ].to_string(index=False)
)


# ==============================
# SLOW MOVERS
# ==============================

print("\n===================================")
print("TOP 10 SLOW-MOVING PRODUCTS")
print("===================================")

slow_movers = product_demand.sort_values(
    "Total_Quantity",
    ascending=True
).head(10)

print(
    slow_movers[
        [
            "Product Name",
            "Total_Quantity",
            "Total_Sales",
            "Number_of_Orders"
        ]
    ].to_string(index=False)
)


# ==============================
# CATEGORY DEMAND
# ==============================

category_demand = (
    df.groupby("Category Name")
    .agg(
        Total_Quantity=("Order Item Quantity", "sum"),
        Total_Sales=("Sales", "sum"),
        Number_of_Orders=("Order Id", "nunique")
    )
    .reset_index()
)

category_demand = category_demand.sort_values(
    "Total_Quantity",
    ascending=False
)

print("\n===================================")
print("TOP 10 CATEGORIES BY DEMAND")
print("===================================")

print(
    category_demand.head(10).to_string(index=False)
)


# ==============================
# DEMAND VARIABILITY
# ==============================

demand_variability = (
    df.groupby("Category Name")["Order Item Quantity"]
    .agg(["mean", "std"])
    .reset_index()
)

demand_variability["Coefficient_of_Variation"] = (
    demand_variability["std"] /
    demand_variability["mean"]
)

demand_variability = demand_variability.sort_values(
    "Coefficient_of_Variation",
    ascending=False
)

print("\n===================================")
print("TOP 10 HIGH DEMAND VARIABILITY CATEGORIES")
print("===================================")

print(
    demand_variability.head(10).to_string(index=False)
)


# ==============================
# REPLENISHMENT PRIORITY
# ==============================

category_demand["Demand_Per_Order"] = (
    category_demand["Total_Quantity"] /
    category_demand["Number_of_Orders"]
)

# High-demand categories receive higher priority
category_demand["Replenishment_Priority"] = pd.qcut(
    category_demand["Total_Quantity"],
    q=3,
    labels=["Low", "Medium", "High"],
    duplicates="drop"
)

print("\n===================================")
print("REPLENISHMENT PRIORITY")
print("===================================")

print(
    category_demand[
        [
            "Category Name",
            "Total_Quantity",
            "Total_Sales",
            "Replenishment_Priority"
        ]
    ].head(15).to_string(index=False)
)


# ==============================
# SAVE ANALYSIS
# ==============================

output_file = "data/inventory_demand_analysis.csv"

category_demand.to_csv(
    output_file,
    index=False
)

print("\nSaved demand-based inventory analysis to:")
print(output_file)

print("\n===================================")
print("INVENTORY / DEMAND ANALYSIS COMPLETED")
print("===================================")

print(
    "\nNOTE: Actual inventory quantities are not available "
    "in the dataset. Therefore, these are demand-based "
    "inventory indicators, not actual stock levels."
)