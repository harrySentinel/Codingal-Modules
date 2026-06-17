import random
import matplotlib.pyplot as plt

population = [random.randint(1, 6) for _ in range(1000)]

print("Central Limit Theorem - Dice Roll Experiment")
print("Population: 1000 dice rolls")
print("Population Mean:", round(sum(population) / len(population), 2))
print()

sample_sizes = [5, 20, 50]
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
fig.suptitle("Central Limit Theorem - Sample Means Distribution", fontsize=12)

for i, size in enumerate(sample_sizes):
    means = []
    for _ in range(200):
        sample = random.sample(population, size)
        means.append(sum(sample) / len(sample))

    axes[i].hist(means, bins=15, color='steelblue', edgecolor='black')
    axes[i].set_title(f"Sample Size = {size}")
    axes[i].set_xlabel("Sample Mean")
    axes[i].set_ylabel("Frequency")
    print(f"Sample size {size} -> Mean of Means: {round(sum(means)/len(means), 2)}")

plt.tight_layout()
plt.savefig("central_limit_theorem.png")
plt.show()
