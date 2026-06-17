import pandas as pd
import numpy as np

data = {
    "Name": ["Aditya", "Riya", None, "Neha", "Rohan", "Priya", "Aman", None],
    "Age": [25, 22, 28, None, 26, 24, None, 30],
    "Salary": [95000, 72000, 88000, 65000, None, 78000, 91000, 55000],
    "City": ["Mumbai", "Delhi", "Mumbai", "Chennai", "Bangalore", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print()
print("Missing Values:")
print(df.isnull().sum())

df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

print("\nAfter Cleaning:")
print(df)
print()
print("Duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Data shape after removing duplicates:", df.shape)
