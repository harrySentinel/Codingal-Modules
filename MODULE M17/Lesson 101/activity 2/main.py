rainy_days = [0, 1, 2, 3, 4, 5]
probabilities = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]

print("Rain Expectation - Number of rainy days in a week")
print()
print("Days   Probability")
for d, p in zip(rainy_days, probabilities):
    print(f"  {d}       {p}")

expected = sum(d * p for d, p in zip(rainy_days, probabilities))
print()
print("Expected rainy days =", round(expected, 2))

variance = sum(p * (d - expected) ** 2 for d, p in zip(rainy_days, probabilities))
print("Variance            =", round(variance, 2))
print("Std Deviation       =", round(variance ** 0.5, 2))
