import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Aditya", "Riya", "Aman", "Neha", "Rohan", "Priya", "Karan", "Sneha"],
    "Math": [92, 78, 85, 60, 74, 95, 55, 88],
    "Science": [88, 82, 79, 65, 70, 91, 60, 85],
    "English": [75, 90, 68, 80, 65, 88, 72, 78],
    "History": [70, 85, 74, 88, 60, 80, 65, 82]
}

df = pd.DataFrame(data)
df["Total"] = df[["Math", "Science", "English", "History"]].sum(axis=1)
df["Average"] = df["Total"] / 4
df["Grade"] = df["Average"].apply(
    lambda x: "A" if x >= 85 else ("B" if x >= 70 else "C")
)

print("Student Report Card:")
print(df)
print()
print("Class Topper:", df.loc[df["Average"].idxmax(), "Name"])
print("Class Average:", round(df["Average"].mean(), 2))
print()
print("Grade Distribution:")
print(df["Grade"].value_counts())

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Student Performance Dashboard", fontsize=14)

axes[0].bar(df["Name"], df["Average"], color=["green" if g == "A" else "orange" if g == "B" else "red" for g in df["Grade"]])
axes[0].set_title("Average Marks")
axes[0].set_ylabel("Average")
axes[0].tick_params(axis='x', rotation=45)

subject_avg = df[["Math", "Science", "English", "History"]].mean()
axes[1].pie(subject_avg, labels=subject_avg.index, autopct="%1.1f%%", startangle=90)
axes[1].set_title("Subject-wise Average")

sns.heatmap(df[["Math", "Science", "English", "History"]].set_index(df["Name"]),
            annot=True, fmt=".0f", cmap="YlGn", ax=axes[2])
axes[2].set_title("Marks Heatmap")

plt.tight_layout()
plt.savefig("capstone_dashboard.png")
plt.show()
