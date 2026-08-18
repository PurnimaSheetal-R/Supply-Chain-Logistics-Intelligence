import pandas as pd
import numpy as np
from scipy import stats

# ==============================
# LOAD DATA
# ==============================

file_path = "data/DataCoSupplyChainDataset.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# ==============================
# DESCRIPTIVE STATISTICS
# ==============================

numeric_columns = [
    "Sales",
    "Order Item Quantity",
    "Days for shipping (real)",
    "Days for shipment (scheduled)"
]

print("\n===================================")
print("DESCRIPTIVE STATISTICS")
print("===================================")

print(df[numeric_columns].describe())


# ==============================
# CORRELATION ANALYSIS
# ==============================

print("\n===================================")
print("CORRELATION MATRIX")
print("===================================")

correlation = df[numeric_columns].corr()

print(correlation)


# ==============================
# IQR OUTLIER ANALYSIS
# ==============================

print("\n===================================")
print("OUTLIER ANALYSIS USING IQR")
print("===================================")

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower) |
        (df[column] > upper)
    ]

    print(
        column,
        "→ Outliers:",
        len(outliers)
    )


# ==============================
# HYPOTHESIS TEST
# ==============================
# Question:
# Is actual shipping duration significantly
# different from scheduled shipping duration?

real_shipping = df["Days for shipping (real)"].dropna()
scheduled_shipping = df["Days for shipment (scheduled)"].dropna()

t_stat, p_value = stats.ttest_rel(
    real_shipping,
    scheduled_shipping
)

print("\n===================================")
print("HYPOTHESIS TEST")
print("===================================")

print("T-statistic:", round(t_stat, 4))
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print(
        "Result: Significant difference between "
        "actual and scheduled shipping duration."
    )
else:
    print(
        "Result: No significant difference between "
        "actual and scheduled shipping duration."
    )


# ==============================
# CONFIDENCE INTERVAL
# ==============================

mean_sales = df["Sales"].mean()
std_sales = df["Sales"].std()
n = df["Sales"].count()

confidence = 0.95

standard_error = std_sales / np.sqrt(n)

margin = stats.t.ppf(
    (1 + confidence) / 2,
    n - 1
) * standard_error

lower_ci = mean_sales - margin
upper_ci = mean_sales + margin

print("\n===================================")
print("95% CONFIDENCE INTERVAL")
print("===================================")

print("Mean Sales:", round(mean_sales, 2))
print("Lower Bound:", round(lower_ci, 2))
print("Upper Bound:", round(upper_ci, 2))


print("\n===================================")
print("STATISTICAL ANALYSIS COMPLETED")
print("===================================")