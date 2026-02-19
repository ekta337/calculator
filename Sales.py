import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For better chart style
sns.set(style="whitegrid")
# Load CSV file
df = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\archive (2)\\sales_data.csv")

# Display first 5 rows
df.head()
# Check dataset info
df.info()

# Check missing values
df.isnull().sum()

# Summary statistics
df.describe()
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)
sales_by_region = df.groupby("Region")["Sales"].sum()
print(sales_by_region)

sales_by_region.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.show()
sales_by_category = df.groupby("Category")["Sales"].sum()

sales_by_category.plot(kind="pie", autopct='%1.1f%%')
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract Month
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)

top_products.plot(kind="bar", color="green")
plt.title("Top 5 Selling Products")
plt.ylabel("Sales")
plt.show()
sns.scatterplot(data=df, x="Quantity", y="Sales")
plt.title("Sales vs Quantity")
plt.show()
