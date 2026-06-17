from fractions import Fraction

total = 52

p_ace = Fraction(4, total)
p_king = Fraction(4, total)
p_heart = Fraction(13, total)
p_face = Fraction(12, total)

print("Deck of Cards - Probability as Fractions")
print()
print("P(Ace)       =", p_ace)
print("P(King)      =", p_king)
print("P(Heart)     =", p_heart)
print("P(Face Card) =", p_face)
print()
print("P(Ace) as decimal =", round(float(p_ace), 4))
print("P(Heart) as %     =", round(float(p_heart) * 100, 1), "%")
