import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

survival_by_class = df.groupby('pclass')['survived'].mean() * 100
survival_by_sex = df.groupby('sex')['survived'].mean() * 100

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(['1st Class', '2nd Class', '3rd Class'], survival_by_class, color=['gold', 'silver', 'brown'])
axes[0].set_title("Survival Rate by Passenger Class")
axes[0].set_ylabel("Survival Rate (%)")

axes[1].bar(survival_by_sex.index, survival_by_sex, color=['blue', 'pink'])
axes[1].set_title("Survival Rate by Gender")
axes[1].set_ylabel("Survival Rate (%)")

plt.tight_layout()
plt.savefig("survival_by_class_gender.png")
plt.show()
