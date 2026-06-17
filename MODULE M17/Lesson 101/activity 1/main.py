import matplotlib.pyplot as plt

outcomes = [0, 1, 2]
pmf = [0.25, 0.50, 0.25]

cdf = []
cumulative = 0
for p in pmf:
    cumulative += p
    cdf.append(cumulative)

print("Coin CDF - Tossing 2 coins")
print()
print("X   PMF    CDF")
for o, p, c in zip(outcomes, pmf, cdf):
    print(f"{o}   {p}    {c}")

print()
print("P(X <= 1) =", cdf[1])
print("P(X <= 2) =", cdf[2])

plt.step(outcomes, cdf, where='post', color='blue', linewidth=2)
plt.scatter(outcomes, cdf, color='red', zorder=5)
plt.title("Coin CDF - 2 Tosses")
plt.xlabel("Number of Heads")
plt.ylabel("Cumulative Probability")
plt.ylim(0, 1.1)
plt.grid(True)
plt.savefig("coin_cdf.png")
plt.show()
