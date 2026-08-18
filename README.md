# SUPPLY CHAIN & LOGISTICS INTELLIGENCE SYSTEM

## 1. Project Overview

This project develops an end-to-end Supply Chain & Logistics Intelligence
System using data analytics, SQL, statistics, forecasting, machine learning
and Power BI.

The project analyzes sales, products, customers, markets, shipping and
delivery performance to identify operational risks and support business
decision-making.

Dataset:
DataCo Smart Supply Chain Dataset

## 2. Data Cleaning & Preparation

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Empty columns
- Invalid or unnecessary fields
- Delivery and shipping-related values

Duplicate rows found: 0.

The completely empty Product Description field was removed during cleaning.
The processed data was then used for SQL analysis, EDA, forecasting and
machine-learning analysis.

## 3. Business Analysis

The project analyzes:

- Sales and profitability
- Product and category performance
- Market and regional performance
- Customer-segment performance
- Shipping-mode performance
- Delivery and late-delivery risk
- Customer and logistics trends

## 4. Supply Chain KPIs

Key KPIs include:

- Total Sales
- Total Profit
- Unique Orders
- Unique Customers
- Average Shipping Duration
- Late Delivery Risk
- Sales by Market
- Sales by Category
- Sales by Customer Segment

## 5. Forecasting

Monthly sales trends were analyzed and a demand-forecasting component was
developed to support future planning and inventory decisions.

Forecast outputs and visualizations are included in the project repository.

## 6. Machine Learning

A late-delivery prediction component was developed to identify orders that
may be at risk of late delivery.

The project includes:

- Late-delivery prediction
- Model evaluation
- Confusion matrix
- Prediction-related analysis

## 7. Power BI Dashboard

An interactive Power BI dashboard was created containing:

- Sales analysis
- Profit analysis
- Order status
- Market analysis
- Product analysis
- Sales trends
- Shipping and delivery analysis
- Geographic analysis
- Average shipping days

Interactive slicers are provided for:

- Market
- Order Region
- Order Status

Power BI dashboard file:
Supply_Chain_Logistics_Dashboard.pbix

## 8. Business Recommendations

1. Improve logistics planning to reduce late-delivery risk.
2. Investigate shipping modes with high delivery risk.
3. Focus inventory and marketing on high-performing categories.
4. Monitor high-performing markets such as Europe and LATAM.
5. Develop targeted strategies for high-value customer segments.
6. Monitor cancelled orders and investigate their causes.
7. Use demand trends and forecasting to improve planning.

## 9. Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- SQLite
- Scikit-learn
- Forecasting
- Power BI
- VS Code
- Git
- GitHub

## 10. Project Structure

supply-chain-logistics-project/
├── data/
├── visualizations/
├── analysis.sql
├── cleaning.py
├── database.py
├── run_sql.py
├── visualization.py
├── README.md
└── Supply_Chain_Logistics_Dashboard.pbix

## 11. Conclusion

The project provides an analytical view of supply-chain performance across
sales, products, customers, markets, shipping and delivery operations.

The analysis highlights delivery performance as an important operational
risk and demonstrates how analytics, forecasting, machine learning and
business intelligence can support better supply-chain decision-making.