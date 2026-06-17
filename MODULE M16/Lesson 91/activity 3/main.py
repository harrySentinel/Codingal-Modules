import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

survival_count = df['survived'].value_counts()
labels = ['Did Not Survive', 'Survived']

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(labels, survival_count, color=['red', 'green'])
axes[0].set_title("Titanic Survival Count")
axes[0].set_ylabel("Number of Passengers")

axes[1].pie(survival_count, labels=labels, autopct='%1.1f%%', colors=['red', 'green'])
axes[1].set_title("Survival Rate")

plt.tight_layout()
plt.savefig("survival_chart.png")
plt.show()
