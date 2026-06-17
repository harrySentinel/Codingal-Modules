import random
import matplotlib.pyplot as plt

bag = ['Red'] * 5 + ['Blue'] * 3 + ['Yellow'] * 2

trials = 1000
results = []

for _ in range(trials):
    results.append(random.choice(bag))

colors = ['Red', 'Blue', 'Yellow']
counts = [results.count(c) for c in colors]

print("After", trials, "picks:")
for color, count in zip(colors, counts):
    print(f"  {color}: {count} times ({round(count/trials*100, 1)}%)")

plt.bar(colors, counts, color=['red', 'blue', 'yellow'])
plt.title("Ball Picking Simulation (1000 trials)")
plt.ylabel("Count")
plt.savefig("ball_simulation.png")
plt.show()
