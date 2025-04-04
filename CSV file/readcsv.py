import pandas as pd

df = pd.read_csv("auto.csv")

df.drop_duplicates(inplace=True)

df.fillna(method='ffill', inplace=True)

most_expensive_car = df.loc[df["price"].idxmax()]
print("Most Expensive Car Company:", most_expensive_car["company"])

toyota_cars = df[df["company"].str.lower() == "toyota"]
print("Toyota Car Details:\n", toyota_cars)

car_count = df["company"].value_counts()
print("Total Cars per Company:\n", car_count)

highest_priced_car = df[df["price"] == df["price"].max()]
print("Highest Priced Car:\n", highest_priced_car)

avg_mileage = df.groupby("company")["average-mileage"].mean()
print("Average Mileage of Each Company:\n", avg_mileage)

sorted_cars = df.sort_values(by="price", ascending=False)
print("Cars Sorted by Price:\n", sorted_cars)
