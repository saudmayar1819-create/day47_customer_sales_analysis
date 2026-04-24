import pandas as pd

# Load data
df = pd.read_csv("customer_sales.csv")

# Clean data
df = df.drop_duplicates()
df = df.dropna()
df = df.reset_index(drop=True)

print("Clean Data:\n")
print(df)
# =========================
# 📊 Analysis
# =========================

# Total Revenue
print("\nTotal Revenue:", df["Sales"].sum())

# Revenue by Product
product_sales = df.groupby("Product")["Sales"].sum()
print("\nRevenue by Product:\n", product_sales)

# Revenue by Customer
customer_sales = df.groupby("Customer")["Sales"].sum()
print("\nRevenue by Customer:\n", customer_sales)

# Top Customer
top_customer = customer_sales.idxmax()
print("\nTop Customer:", top_customer)

# Best Product
best_product = product_sales.idxmax()
print("Best Product:", best_product)

import matplotlib.pyplot as plt

# Product chart
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.show()

# Customer chart
customer_sales.plot(kind="bar")
plt.title("Sales by Customer")
plt.show()