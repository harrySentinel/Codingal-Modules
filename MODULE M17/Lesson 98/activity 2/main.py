p_A = 0.5
p_B = 0.4
p_A_and_B = p_A * p_B

print("Tossing two coins independently")
print()
print("P(Heads on Coin 1) = P(A) =", p_A)
print("P(Heads on Coin 2) = P(B) =", p_B)
print()
print("P(A ∩ B) = P(A) × P(B)  [since events are independent]")
print("P(A ∩ B) =", p_A, "×", p_B, "=", p_A_and_B)
print()

p_math = 0.6
p_science = 0.5
p_both = 0.3

print("Aditya passes Math    -> P(M) =", p_math)
print("Aditya passes Science -> P(S) =", p_science)
print("Aditya passes both    -> P(M∩S) =", p_both)
print()
print("Are they independent?", p_math * p_science == p_both)
