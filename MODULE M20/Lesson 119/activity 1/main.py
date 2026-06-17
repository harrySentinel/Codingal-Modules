import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = {
    "CreditScore":    [619, 608, 502, 699, 850, 645, 822, 376, 501, 684,
                       528, 497, 476, 549, 635, 616, 653, 422, 549, 715],
    "Geography":      ["France","Spain","France","France","Spain","Spain","France",
                       "Germany","France","France","Germany","France","Germany",
                       "France","Spain","Germany","Spain","France","Germany","France"],
    "Gender":         ["Female","Female","Female","Female","Female","Male","Male","Female",
                       "Male","Male","Male","Female","Male","Female","Male","Male",
                       "Female","Male","Male","Female"],
    "Age":            [42,41,42,39,43,44,50,29,44,27,31,24,34,25,35,45,58,36,44,48],
    "Balance":        [0,83808,159660,0,125510,113755,0,115046,142051,134603,
                       102016,76390,0,50670,0,143129,132602,0,96270,0],
    "NumProducts":    [1,1,3,2,1,2,2,4,2,1,2,2,1,2,2,1,1,2,2,1],
    "HasCrCard":      [1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0],
    "IsActiveMember": [1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0],
    "Salary":         [101348,112542,113931,93826,79084,149756,10062,119346,74940,71725,
                       80181,71725,44350,68759,44350,149756,116702,65951,44350,113931],
    "Exited":         [1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
}

df = pd.DataFrame(data)
print("Churn Modelling Dataset:")
print(df.head())
print()
print("Customers who left (Exited=1):", df["Exited"].sum())
print("Customers who stayed (Exited=0):", (df["Exited"] == 0).sum())
print()
print("Missing values:", df.isnull().sum().sum())

le = LabelEncoder()
df["Geography"] = le.fit_transform(df["Geography"])
df["Gender"] = le.fit_transform(df["Gender"])

X = df.drop("Exited", axis=1).values
y = df["Exited"].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print()
print("Data preprocessed and split:")
print("Training samples:", len(X_train))
print("Testing samples: ", len(X_test))

np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)
print()
print("Data saved. Ready for ANN training in Part 2!")
