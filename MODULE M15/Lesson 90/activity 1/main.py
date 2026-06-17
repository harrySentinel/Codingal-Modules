import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"])
df["Species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("First 5 rows:")
print(df.head())
print()

print("Missing Values:")
print(df.isnull().sum())
print()

print("Basic Statistics:")
print(df.describe())
print()

print("Species Count:")
print(df["Species"].value_counts())
print()

print("Average per Species:")
print(df.groupby("Species").mean())

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Iris Dataset Analysis", fontsize=14)

for species in df["Species"].unique():
    subset = df[df["Species"] == species]
    axes[0].scatter(subset["Sepal Length"], subset["Sepal Width"], label=species, s=60)
axes[0].set_title("Sepal Length vs Width")
axes[0].set_xlabel("Sepal Length (cm)")
axes[0].set_ylabel("Sepal Width (cm)")
axes[0].legend()

for species in df["Species"].unique():
    subset = df[df["Species"] == species]
    axes[1].scatter(subset["Petal Length"], subset["Petal Width"], label=species, s=60)
axes[1].set_title("Petal Length vs Width")
axes[1].set_xlabel("Petal Length (cm)")
axes[1].set_ylabel("Petal Width (cm)")
axes[1].legend()

sns.boxplot(data=df, x="Species", y="Petal Length", palette="Set2", ax=axes[2])
axes[2].set_title("Petal Length by Species")

plt.tight_layout()
plt.savefig("iris_capstone.png")
plt.show()
