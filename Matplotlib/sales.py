import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

plt.scatter(df["month_number"], df["toothpaste"], color="red", label="Toothpaste Sales")
plt.xlabel("Month Number")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales per Month")
plt.legend()
plt.grid()
plt.show()

plt.bar(df["month_number"] - 0.2, df["face_cream"], width=0.4, label="Face Cream", color="blue")
plt.bar(df["month_number"] + 0.2, df["facewash"], width=0.4, label="Face Wash", color="green")
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.title("Face Cream & Face Wash Sales per Month")
plt.legend()
plt.show()

total_sales = df[["face_cream", "facewash", "toothpaste", "bathing_soap", "shampoo", "moisturizer"]].sum()
plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", startangle=140)
plt.title("Total Sales Distribution (Last Year)")
plt.show()
