-- ============================================
-- SUPPLY CHAIN LOGISTICS INTELLIGENCE PROJECT
-- STEP 4: SQL ANALYSIS
-- ============================================


-- 1. TOTAL SALES
SELECT
    SUM(Sales) AS Total_Sales
FROM supply_chain;


-- 2. TOTAL PROFIT
SELECT
    SUM([Order Profit Per Order]) AS Total_Profit
FROM supply_chain;


-- 3. TOTAL UNIQUE ORDERS
SELECT
    COUNT(DISTINCT [Order Id]) AS Total_Orders
FROM supply_chain;


-- 4. TOTAL UNIQUE CUSTOMERS
SELECT
    COUNT(DISTINCT [Customer Id]) AS Total_Customers
FROM supply_chain;


-- 5. SALES BY MARKET
SELECT
    Market,
    SUM(Sales) AS Total_Sales
FROM supply_chain
GROUP BY Market
ORDER BY Total_Sales DESC;


-- 6. TOP 10 PRODUCT CATEGORIES BY SALES
SELECT TOP 10
    [Category Name],
    SUM(Sales) AS Total_Sales
FROM supply_chain
GROUP BY [Category Name]
ORDER BY Total_Sales DESC;


-- 7. PROFIT BY CUSTOMER SEGMENT
SELECT
    [Customer Segment],
    SUM([Order Profit Per Order]) AS Total_Profit
FROM supply_chain
GROUP BY [Customer Segment]
ORDER BY Total_Profit DESC;


-- 8. SALES BY SHIPPING MODE
SELECT
    [Shipping Mode],
    SUM(Sales) AS Total_Sales
FROM supply_chain
GROUP BY [Shipping Mode]
ORDER BY Total_Sales DESC;


-- 9. LATE DELIVERY RISK BY SHIPPING MODE
SELECT
    [Shipping Mode],
    AVG(CAST(Late_delivery_risk AS FLOAT)) * 100
        AS Late_Delivery_Risk_Percentage
FROM supply_chain
GROUP BY [Shipping Mode]
ORDER BY Late_Delivery_Risk_Percentage DESC;


-- 10. DELIVERY STATUS ANALYSIS
SELECT
    [Delivery Status],
    COUNT(*) AS Number_of_Orders
FROM supply_chain
GROUP BY [Delivery Status]
ORDER BY Number_of_Orders DESC;


-- 11. SALES BY CUSTOMER SEGMENT
SELECT
    [Customer Segment],
    SUM(Sales) AS Total_Sales
FROM supply_chain
GROUP BY [Customer Segment]
ORDER BY Total_Sales DESC;


-- 12. AVERAGE ORDER VALUE
SELECT
    AVG(Sales) AS Average_Order_Value
FROM supply_chain;


-- 13. TOP 10 CUSTOMERS BY SALES
SELECT TOP 10
    [Customer Id],
    SUM(Sales) AS Total_Sales
FROM supply_chain
GROUP BY [Customer Id]
ORDER BY Total_Sales DESC;


-- 14. ORDERS BY ORDER STATUS
SELECT
    [Order Status],
    COUNT(DISTINCT [Order Id]) AS Number_of_Orders
FROM supply_chain
GROUP BY [Order Status]
ORDER BY Number_of_Orders DESC;


-- 15. SALES BY DEPARTMENT
SELECT
    [Department Name],
    SUM(Sales) AS Total_Sales
FROM supply_chain
GROUP BY [Department Name]
ORDER BY Total_Sales DESC;


-- ============================================
-- END OF SQL ANALYSIS
-- ============================================