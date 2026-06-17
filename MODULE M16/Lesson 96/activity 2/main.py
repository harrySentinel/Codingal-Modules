import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

print("Iris Dataset Survey:")
print("Total Flowers:", len(df))
print()
print("Species:", df['species'].unique().tolist())
print()
print("Count per Species:")
print(df['species'].value_counts())
print()
print("Average Measurements per Species:")
print(df.groupby('species').mean().round(2))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

for species in df['species'].unique():
    subset = df[df['species'] == species]
    axes[0].scatter(subset['sepal_length'], subset['sepal_width'], label=species, s=50)
axes[0].set_title("Sepal Length vs Width")
axes[0].set_xlabel("Sepal Length")
axes[0].set_ylabel("Sepal Width")
axes[0].legend()

sns.boxplot(data=df, x='species', y='petal_length', palette='Set2', ax=axes[1])
axes[1].set_title("Petal Length by Species")

plt.tight_layout()
plt.savefig("iris_survey.png")
plt.show()
