import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = {
    "Name": ["Aditya", "Riya", "Aman", None, "Rohan", "Priya"],
    "Age": [25, 22, None, 28, 26, 24],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune", None, "Delhi"],
    "Salary": [95000, 72000, 88000, 65000, 78000, None],
    "Gender": ["Male", "Female", "Male", "Male", "Male", "Female"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print()
print("Missing Values:")
print(df.isnull().sum())

df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna(df["City"].mode()[0], inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

le = LabelEncoder()
df["Gender_encoded"] = le.fit_transform(df["Gender"])
df["City_encoded"] = le.fit_transform(df["City"])

scaler = StandardScaler()
df["Age_scaled"] = scaler.fit_transform(df[["Age"]])
df["Salary_scaled"] = scaler.fit_transform(df[["Salary"]])

print("After Preprocessing:")
print(df)
