import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Area_sqft": [500, 750, 1000, 1200, 1500, 800, 950, 1100, 1300, 600],
    "Bedrooms": [1, 2, 3, 3, 4, 2, 2, 3, 3, 1],
    "Location": ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Mumbai",
                 "Delhi", "Bangalore", "Mumbai", "Delhi", "Bangalore"],
    "Rent": [15000, 20000, 35000, 28000, 55000, 18000, 22000, 38000, 30000, 12000]
}

df = pd.DataFrame(data)

print("Housing Data:")
print(df)
print()
print("Average Rent by Location:")
print(df.groupby("Location")["Rent"].mean())

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.barplot(data=df, x="Location", y="Rent", palette="Blues_d")
plt.title("Avg Rent by Location")

plt.subplot(1, 3, 2)
sns.scatterplot(data=df, x="Area_sqft", y="Rent", hue="Location", s=100)
plt.title("Area vs Rent")

plt.subplot(1, 3, 3)
sns.boxplot(data=df, x="Bedrooms", y="Rent", palette="Set2")
plt.title("Rent by Bedrooms")

plt.tight_layout()
plt.savefig("housing_rent.png")
plt.show()
