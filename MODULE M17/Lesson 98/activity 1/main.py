p_A = 0.4
p_B = 0.3
p_A_and_B = 0.1

p_A_or_B = p_A + p_B - p_A_and_B

print("Event A: Student likes Cricket   -> P(A) =", p_A)
print("Event B: Student likes Football  -> P(B) =", p_B)
print("Both Cricket and Football        -> P(A∩B) =", p_A_and_B)
print()
print("P(A ∪ B) = P(A) + P(B) - P(A∩B)")
print("P(A ∪ B) =", p_A, "+", p_B, "-", p_A_and_B, "=", p_A_or_B)
print()
print(round(p_A_or_B * 100, 1), "% of students like Cricket OR Football")
