import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Patient": ["Aditya", "Riya", "Aman", "Neha", "Rohan", "Priya", "Karan", "Sneha", "Vijay", "Meena"],
    "Age": [25, 45, 60, 35, 50, 40, 55, 30, 65, 48],
    "Fasting_Sugar": [90, 130, 180, 95, 145, 110, 160, 88, 200, 125],
    "PostMeal_Sugar": [120, 175, 230, 130, 195, 150, 210, 115, 260, 170],
    "Status": ["Normal", "PreDiabetic", "Diabetic", "Normal", "Diabetic",
               "PreDiabetic", "Diabetic", "Normal", "Diabetic", "PreDiabetic"]
}

df = pd.DataFrame(data)

print("Blood Sugar Analysis:")
print(df)
print()
print("Count by Status:")
print(df["Status"].value_counts())
print()
print("Average Fasting Sugar by Status:")
print(df.groupby("Status")["Fasting_Sugar"].mean())

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle("Blood Sugar Level Analysis", fontsize=14)

colors = {"Normal": "green", "PreDiabetic": "orange", "Diabetic": "red"}
for status, group in df.groupby("Status"):
    axes[0].scatter(group["Age"], group["Fasting_Sugar"],
                    label=status, color=colors[status], s=100)
axes[0].axhline(y=100, color='gray', linestyle='--', label='Normal limit')
axes[0].set_title("Age vs Fasting Sugar")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Fasting Sugar (mg/dL)")
axes[0].legend()

df["Status"].value_counts().plot(kind='pie', autopct='%1.1f%%',
    colors=["green", "orange", "red"], ax=axes[1])
axes[1].set_title("Patient Distribution")
axes[1].set_ylabel("")

sns.boxplot(data=df, x="Status", y="PostMeal_Sugar",
            palette=colors, ax=axes[2])
axes[2].set_title("Post-Meal Sugar by Status")

plt.tight_layout()
plt.savefig("blood_sugar_analysis.png")
plt.show()
