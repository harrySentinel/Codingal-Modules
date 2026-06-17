import matplotlib.pyplot as plt

outcomes = [0, 1, 2]
probs = [0.25, 0.50, 0.25]
labels = ['0 Heads (TT)', '1 Head (HT or TH)', '2 Heads (HH)']

print("Coin Toss PMF - Tossing 2 coins")
print()
for o, p, l in zip(outcomes, probs, labels):
    print(f"P(X = {o}) = {p}  [{l}]")

print()
expected = sum(o * p for o, p in zip(outcomes, probs))
print("Expected number of Heads:", expected)

plt.bar(labels, probs, color=['orange', 'green', 'orange'], edgecolor='black')
plt.title("Coin PMF - 2 Tosses")
plt.ylabel("Probability")
plt.savefig("coin_pmf.png")
plt.show()
