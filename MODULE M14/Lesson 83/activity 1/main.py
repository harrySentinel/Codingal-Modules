import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Temperature": [15, 17, 22, 28, 34, 37, 35, 34, 30, 25, 19, 14],
    "Humidity": [60, 58, 55, 45, 40, 65, 80, 85, 70, 55, 62, 65],
    "Rainfall_mm": [10, 8, 12, 5, 3, 80, 200, 180, 100, 30, 15, 12]
}

df = pd.DataFrame(data)

print("Weather Data:")
print(df)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Weather Data Visualization - Mumbai", fontsize=14)

axes[0, 0].plot(df["Month"], df["Temperature"], marker='o', color='red')
axes[0, 0].set_title("Monthly Temperature")
axes[0, 0].set_ylabel("Temp (°C)")
axes[0, 0].grid(True)

axes[0, 1].bar(df["Month"], df["Rainfall_mm"], color="steelblue")
axes[0, 1].set_title("Monthly Rainfall")
axes[0, 1].set_ylabel("Rainfall (mm)")

axes[1, 0].plot(df["Month"], df["Humidity"], marker='s', color='green')
axes[1, 0].set_title("Monthly Humidity")
axes[1, 0].set_ylabel("Humidity (%)")
axes[1, 0].grid(True)

sns.heatmap(df[["Temperature", "Humidity", "Rainfall_mm"]].corr(),
            annot=True, cmap="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("weather_visualization.png")
plt.show()
