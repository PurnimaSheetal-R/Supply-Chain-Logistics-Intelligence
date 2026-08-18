import sqlite3
import pandas as pd

db_path = r"C:\Users\sanka\OneDrive\Desktop\project\data\supply_chain.db"

conn = sqlite3.connect(db_path)

import sqlite3
import pandas as pd

db_path = r"C:\Users\sanka\OneDrive\Desktop\project\data\supply_chain.db"

conn = sqlite3.connect(db_path)

queries = {
    "TOTAL SALES": """
        SELECT ROUND(SUM(Sales), 2) AS Total_Sales
        FROM supply_chain;
    """,

    "TOTAL PROFIT": """
        SELECT ROUND(SUM("Order Profit Per Order"), 2) AS Total_Profit
        FROM supply_chain;
    """,

    "ORDERS AND CUSTOMERS": """
        SELECT
            COUNT(DISTINCT "Order Id") AS Unique_Orders,
            COUNT(DISTINCT "Customer Id") AS Unique_Customers
        FROM supply_chain;
    """,

    "SALES BY MARKET": """
        SELECT Market,
               ROUND(SUM(Sales), 2) AS Total_Sales
        FROM supply_chain
        GROUP BY Market
        ORDER BY Total_Sales DESC;
    """,

    "TOP 10 CATEGORIES": """
        SELECT "Category Name",
               ROUND(SUM(Sales), 2) AS Total_Sales
        FROM supply_chain
        GROUP BY "Category Name"
        ORDER BY Total_Sales DESC
        LIMIT 10;
    """,

    "SALES BY SHIPPING MODE": """
        SELECT "Shipping Mode",
               ROUND(SUM(Sales), 2) AS Total_Sales
        FROM supply_chain
        GROUP BY "Shipping Mode"
        ORDER BY Total_Sales DESC;
    """,

    "LATE DELIVERY RISK": """
        SELECT "Shipping Mode",
               ROUND(AVG(Late_delivery_risk) * 100, 2)
               AS Late_Delivery_Risk_Percentage
        FROM supply_chain
        GROUP BY "Shipping Mode"
        ORDER BY Late_Delivery_Risk_Percentage DESC;
    """,

    "DELIVERY STATUS": """
        SELECT "Delivery Status",
               COUNT(*) AS Number_of_Orders
        FROM supply_chain
        GROUP BY "Delivery Status"
        ORDER BY Number_of_Orders DESC;
    """,

    "CUSTOMER SEGMENT": """
        SELECT "Customer Segment",
               ROUND(SUM(Sales), 2) AS Total_Sales,
               ROUND(SUM("Order Profit Per Order"), 2) AS Total_Profit
        FROM supply_chain
        GROUP BY "Customer Segment"
        ORDER BY Total_Sales DESC;
    """
}

for title, query in queries.items():

    print("\n===================================")
    print(title)
    print("===================================")

    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))

conn.close()

print("\n===================================")
print("ALL SQL ANALYSIS COMPLETED")
print("===================================")