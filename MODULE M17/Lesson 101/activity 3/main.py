import matplotlib.pyplot as plt

calls = [0, 1, 2, 3, 4, 5]
probabilities = [0.05, 0.15, 0.30, 0.25, 0.15, 0.10]

expected_calls = sum(c * p for c, p in zip(calls, probabilities))
variance = sum(p * (c - expected_calls) ** 2 for c, p in zip(calls, probabilities))

print("Call Center - Expected Calls per Minute")
print()
print("Calls   Probability")
for c, p in zip(calls, probabilities):
    print(f"  {c}       {p}")

print()
print("Expected Calls per Minute:", round(expected_calls, 2))
print("Variance:                 ", round(variance, 2))
print("Std Deviation:            ", round(variance ** 0.5, 2))

plt.bar(calls, probabilities, color='teal', edgecolor='black')
plt.title("Expected Calls - Probability Distribution")
plt.xlabel("Number of Calls")
plt.ylabel("Probability")
plt.savefig("expected_calls.png")
plt.show()
