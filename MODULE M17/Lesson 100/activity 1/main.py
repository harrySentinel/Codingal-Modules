p_strep = 0.30
p_sore_throat_given_strep = 0.90
p_sore_throat_given_no_strep = 0.20
p_no_strep = 1 - p_strep

p_sore_throat = (p_sore_throat_given_strep * p_strep) + (p_sore_throat_given_no_strep * p_no_strep)

print("Step Throat Diagnosis - Bayes Theorem (Part 1)")
print()
print("P(Strep)                    =", p_strep)
print("P(Sore Throat | Strep)      =", p_sore_throat_given_strep)
print("P(Sore Throat | No Strep)   =", p_sore_throat_given_no_strep)
print()
print("P(Sore Throat) =", round(p_sore_throat, 3))
