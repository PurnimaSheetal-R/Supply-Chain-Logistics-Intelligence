import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load dataset
file_path = "data/DataCoSupplyChainDataset.csv"
df = pd.read_csv(file_path, encoding="latin1")

print("Dataset loaded successfully!")

# Convert order date to datetime
df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

# Monthly sales aggregation
monthly_sales = (
    df.set_index("order date (DateOrders)")
      .resample("ME")["Sales"]
      .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# Time-aware train/test split
test_size = 6

train = monthly_sales.iloc[:-test_size]
test = monthly_sales.iloc[-test_size:]

print("\nTraining months:", len(train))
print("Testing months:", len(test))

# Naive baseline
naive_forecast = pd.Series(
    train.iloc[-1],
    index=test.index
)

baseline_mae = mean_absolute_error(test, naive_forecast)
baseline_rmse = np.sqrt(mean_squared_error(test, naive_forecast))

print("\n===== NAIVE BASELINE =====")
print("MAE:", round(baseline_mae, 2))
print("RMSE:", round(baseline_rmse, 2))

# Exponential Smoothing model
model = ExponentialSmoothing(
    train,
    trend="add",
    seasonal="add",
    seasonal_periods=12
)

fitted_model = model.fit(optimized=True)

forecast = fitted_model.forecast(test_size)

# Evaluation
mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("\n===== EXPONENTIAL SMOOTHING =====")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# Compare actual vs forecast
comparison = pd.DataFrame({
    "Actual": test,
    "Forecast": forecast
})

print("\n===== ACTUAL VS FORECAST =====")
print(comparison)

# Plot
plt.figure(figsize=(12, 6))

plt.plot(train.index, train.values, label="Training Sales")
plt.plot(test.index, test.values, label="Actual Sales")
plt.plot(test.index, forecast.values, label="Forecast")

plt.title("Monthly Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.tight_layout()

# Save chart
output_path = "visualizations/monthly_sales_forecast.png"
plt.savefig(output_path)

plt.show()

print("\nForecast chart saved to:")
print(output_path)

print("\n===================================")
print("DEMAND FORECASTING COMPLETED")
print("===================================")