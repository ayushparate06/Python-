import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales_data.csv")

# a) Line Plot - Total Profit
plt.figure()
plt.plot(df['Month'], df['TotalProfit'], marker='o')
plt.title("Total Profit Per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()


# b) Multiline Plot - All Product Sales
plt.figure()
plt.plot(df['Month'], df['FaceCream'], label='Face Cream')
plt.plot(df['Month'], df['FaceWash'], label='Face Wash')
plt.plot(df['Month'], df['Toothpaste'], label='Toothpaste')
plt.plot(df['Month'], df['BathingSoap'], label='Bathing Soap')
plt.plot(df['Month'], df['Shampoo'], label='Shampoo')
plt.plot(df['Month'], df['Moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.grid()
plt.show()


# c) Bar Chart - Face Cream & Face Wash
plt.figure()
width = 0.35
x = range(len(df['Month']))

plt.bar(x, df['FaceCream'], width=width)
plt.bar([i + width for i in x], df['FaceWash'], width=width)

plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Face Cream vs Face Wash Sales")
plt.xticks([i + width/2 for i in x], df['Month'])
plt.show()


# d) Pie Chart - Total Sales per Product (Yearly)
total_sales = [
    df['FaceCream'].sum(),
    df['FaceWash'].sum(),
    df['Toothpaste'].sum(),
    df['BathingSoap'].sum(),
    df['Shampoo'].sum(),
    df['Moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution (Yearly)")
plt.show()