import pandas as pd

data = {
    "Name": ["Aditya Srivastava", "Riya Sharma", "Aman Gupta", "Neha Verma", "Rohan Mehta"],
    "Age": [25, 22, 28, 24, 26],
    "City": ["Mumbai", "Delhi", "Pune", "Chennai", "Bangalore"],
    "Salary": [95000, 72000, 88000, 65000, 78000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print()
print("Shape:", df.shape)
print()
print("Basic Stats:")
print(df.describe())
print()
print("Employees from Mumbai or Delhi:")
print(df[df["City"].isin(["Mumbai", "Delhi"])])
print()
print("Sorted by Salary:")
print(df.sort_values("Salary", ascending=False))
