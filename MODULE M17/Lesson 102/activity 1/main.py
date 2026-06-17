import random
import matplotlib.pyplot as plt

all_puppies = [round(random.uniform(2.0, 8.0), 1) for _ in range(200)]

print("Puppies Dataset - Population (200 puppies)")
print("Population Mean Weight:", round(sum(all_puppies) / len(all_puppies), 2), "kg")
print()

sample_means = []
for _ in range(50):
    sample = random.sample(all_puppies, 20)
    sample_means.append(round(sum(sample) / len(sample), 2))

print("Taking 50 samples of size 20 each:")
print("Sample Means:", sample_means[:10], "...")
print()
print("Mean of Sample Means:", round(sum(sample_means) / len(sample_means), 2), "kg")

plt.hist(sample_means, bins=10, color='orange', edgecolor='black')
plt.title("Distribution of Sample Means (Puppies Weight)")
plt.xlabel("Sample Mean Weight (kg)")
plt.ylabel("Frequency")
plt.savefig("puppies_sampling.png")
plt.show()
