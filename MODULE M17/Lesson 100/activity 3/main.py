import matplotlib.pyplot as plt

outcomes = [1, 2, 3, 4, 5, 6]
probability = 1 / 6

print("Dice Roll - Probability Mass Function (PMF)")
print()
for face in outcomes:
    print(f"P(X = {face}) = {round(probability, 4)}")

print()
print("P(X = even) =", round(3 * probability, 4))
print("P(X > 4)    =", round(2 * probability, 4))

plt.bar(outcomes, [probability] * 6, color='steelblue', edgecolor='black')
plt.title("Dice Roll PMF")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.ylim(0, 0.3)
plt.xticks(outcomes)
plt.savefig("dice_pmf.png")
plt.show()
