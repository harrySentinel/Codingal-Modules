import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025],
    "India":    [870, 930, 1000, 1095, 1180, 1270, 1380, 1430],
    "China":    [1140, 1200, 1260, 1300, 1340, 1370, 1400, 1410],
    "USA":      [250, 265, 280, 295, 310, 320, 331, 340],
    "World":    [5300, 5700, 6100, 6500, 6900, 7300, 7800, 8000]
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].plot(df["Year"], df["India"], marker='o', label="India", color="orange")
axes[0].plot(df["Year"], df["China"], marker='s', label="China", color="red")
axes[0].plot(df["Year"], df["USA"], marker='^', label="USA", color="blue")
axes[0].set_title("Population Growth by Country (in millions)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Population (millions)")
axes[0].legend()
axes[0].grid(True)

axes[1].bar(df["Year"].astype(str), df["World"], color="steelblue")
axes[1].set_title("World Population Growth (in millions)")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Population (millions)")

plt.tight_layout()
plt.savefig("population_growth.png")
plt.show()
