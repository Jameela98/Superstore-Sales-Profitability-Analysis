# Superstore-Sales-Profitability-Analysis

## Overview

This project analyzes a retail Superstore dataset to understand the factors that drive sales and profitability. The analysis focuses on identifying trends, evaluating business performance across categories and regions, and explores how discounts, products, and customer behavior impact profit.

The project covers the complete data analysis workflow, including data cleaning, feature engineering, exploratory data analysis (EDA), and business insights generation.

---

## Business Objective

The main objective of this analysis is to answer the following questions:

- How have sales and profits changed over time?
- Which product categories and sub-categories perform best?
- Which regions generate the highest profits?
- How do discounts affect profitability?
- Which products contribute most to profits and losses?
- Who are the most profitable customers?

---

## Dataset Source

The dataset used in this project was obtained from Kaggle and contains retail transaction data from a Superstore business. The dataset was used for educational and portfolio development purposes.

---

## Dataset Description

The dataset contains retail transaction data, including:

- Order information (Order ID, Order Date, Ship Date)
- Customer details (Customer Name, Segment)
- Product information (Product ID,Product Name, Category, Sub-Category)
- Sales, profit, and discount values
- Geographic information (regions and cities)

---

## Data Cleaning

Before analysis, the dataset required several preprocessing steps:

- Removed duplicate records, including duplicates based on Row ID 
- Dropped unnecessary columns (Postal Code, Row ID)
- Converted date columns (Order Date, Ship Date) to datetime format
- Handled missing values :  
    - Handled missing values in Sales and Profit using median imputation
    - Recovered missing Order Dates using records from the same Order ID (Reconstructed missing Order Dates using forward/backward fill grouped by Order ID)
    - Removed remaining rows with missing Order Dates
  
This ensured the dataset was clean, consistent, and ready for analysis.

---

## Feature Engineering

New features were created from date columns:

- Year (Order)
- Month (Order)
- Year (Ship)
- Month (Ship)

These features were used to analyze sales and profit trends over time.

---

## Exploratory Data Analysis

The analysis was divided into several areas:

###  Time Analysis
- Analyzed monthly and yearly trends for both orders and shipping
- Order date vs. shipping date analysis

###  Shipping Analysis
- Profitability by shipping mode
- Profitability by region and shipping method

###  Category Analysis
- Compared Sales and Profit across product categories
- Profit by sub-category

###  Regional Analysis
- Evaluated profit distribution across different regions
- Evaluated profit distribution across different by category and region
- Analyzed top-performing cities based on sales

###  Discount Analysis
- Relationship between discount and profit to study how discounts impact profitability
- Average profit across discount levels

###  Product Analysis
- Identified top 10 most profitable products
- Identified top 10 loss-making products

###  Customer Analysis
- Ranked customers based on total profit contribution

---

## Key Insights

### 1. Sales Exhibit Seasonal Trends

Monthly and yearly sales patterns indicate that demand changes throughout the year, with certain periods generating stronger sales than others.

**Recommendation:** Use historical trends to improve inventory planning and promotional activities.

---

### 2. Sales Growth Does Not Always Lead to Higher Profit

Some categories generate notable sales but contribute less to overall profit.

**Recommendation:** Focus on profitability in addition to sales volume when evaluating business performance.

---

### 3. Profitability Varies Across Product Sub-Categories

Some sub-categories consistently perform better than others in terms of profit generation.

**Recommendation:** Increase focus on high-performing sub-categories and review strategies for underperforming ones.

---

### 4. Regional Performance Varies Significantly

Profitability differs across regions and cities, indicating that some regions perform much better than others.

**Recommendation:** Investigate underperforming locations and identify opportunities for improvement.

---

### 5. High Discounts Negatively Impact Profitability

A strong negative relationship exists between discount levels and profit. Higher discounts frequently result in lower profits and, in some cases, losses.

**Recommendation:** Review discount strategies and evaluate the effectiveness of high-discount promotions.

---

### 6. A Small Number of Products Drive Losses

Several products consistently generate negative profits.

**Recommendation:** Review pricing, discounts, and operational costs associated with loss-making products.

---

### 7. Profit Contribution Is Concentrated Among a Limited Number of Customers

A relatively small group of customers contributes a significant portion of total profit.

**Recommendation:** Develop retention strategies and loyalty programs for high-value customers.

---

## Conclusion

This analysis of the Superstore dataset helped uncover the main drivers behind the company’s profitability.

While sales show steady growth over time, profit is not always aligned with sales performance. The analysis clearly shows that discount strategy plays a critical role in overall profitability, where higher discounts often lead to reduced profits or even losses.

In addition, performance varies significantly across categories, regions, and products, highlighting that not all sales contribute equally to business success. A small group of products and customers has a strong influence on overall profit, which indicates both opportunity and risk in concentration.

Overall, the results suggest that improving discount policies, optimizing the product mix, and focusing on high-value customers can significantly enhance profitability.

---

## Tools Used

- Python ( Pandas NumPy)
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Future Improvements

Potential next steps for this project include:

- Creating an interactive Tableau or Power BI dashboard
- Building predictive models for sales forecasting
- Performing customer segmentation analysis
- Developing profitability prediction models

---

## Author

Jameela Smadi

Data Analysis Project – Superstore Sales & Profitability Analysis
