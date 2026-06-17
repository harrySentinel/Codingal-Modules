p_A = 0.6
p_B_given_A = 0.5

p_A_and_B = p_A * p_B_given_A

print("Multiplication Rule: P(A ∩ B) = P(A) × P(B|A)")
print()
print("Aditya attempts Question 1 -> P(A) =", p_A)
print("P(attempts Q2 | attempted Q1) = P(B|A) =", p_B_given_A)
print()
print("P(attempts both) = P(A) × P(B|A) =", p_A, "×", p_B_given_A, "=", p_A_and_B)
print()

p_card1_king = 4/52
p_card2_king_given_card1_king = 3/51

p_both_kings = p_card1_king * p_card2_king_given_card1_king
print("Drawing 2 Kings from a deck (without replacement):")
print("P(both Kings) =", round(p_both_kings, 4))
