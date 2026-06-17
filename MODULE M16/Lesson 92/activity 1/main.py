import pandas as pd

data = {
    "Destination": ["Paris", "Tokyo", "New York", "Dubai", "London"],
    "Days": [5, 7, 4, 6, 3],
    "Hotel_per_day": [8000, 10000, 12000, 9000, 11000],
    "Flight_cost": [45000, 60000, 55000, 30000, 40000]
}

df = pd.DataFrame(data)
df["Total_Hotel"] = df["Days"] * df["Hotel_per_day"]
df["Total_Cost"] = df["Total_Hotel"] + df["Flight_cost"]

print("Travel Itinerary Planner:")
print(df)
print()
print("Cheapest Trip:  ", df.loc[df["Total_Cost"].idxmin(), "Destination"])
print("Most Expensive: ", df.loc[df["Total_Cost"].idxmax(), "Destination"])
print("Average Trip Cost: ₹", round(df["Total_Cost"].mean(), 2))
print()
print("Sorted by Total Cost:")
print(df[["Destination", "Total_Cost"]].sort_values("Total_Cost"))
