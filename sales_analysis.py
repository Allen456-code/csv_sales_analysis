import pandas as pd
import matplotlib.pyplot as plt

file_name = "sales_data.csv"
df = pd.read_csv(file_name)

print("First 5 rows of the dataset:")
print(df.head())

print("\nColumn Names in the dataset:")
print(df.columns)

grouped_data = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:")
print(grouped_data)

plt.figure(figsize=(8, 5))
grouped_data.plot(kind="bar", color="skyblue")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
