p_A = 3/6
p_B = 2/6

p_A_or_B = p_A + p_B

print("Rolling a dice")
print()
print("Event A: Getting an Odd number (1,3,5) -> P(A) =", round(p_A, 2))
print("Event B: Getting a number > 4 (5,6)    -> P(B) =", round(p_B, 2))
print()
print("Are A and B mutually exclusive? No (5 is in both)")
print()

p_A_and_B = 1/6
p_A_or_B_corrected = p_A + p_B - p_A_and_B

print("Addition Rule: P(A∪B) = P(A) + P(B) - P(A∩B)")
print("P(A∪B) =", round(p_A, 2), "+", round(p_B, 2), "-", round(p_A_and_B, 2), "=", round(p_A_or_B_corrected, 2))
