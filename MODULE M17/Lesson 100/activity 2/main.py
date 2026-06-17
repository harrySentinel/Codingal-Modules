p_strep = 0.30
p_sore_throat_given_strep = 0.90
p_sore_throat_given_no_strep = 0.20
p_no_strep = 1 - p_strep

p_sore_throat = (p_sore_throat_given_strep * p_strep) + (p_sore_throat_given_no_strep * p_no_strep)

p_strep_given_sore_throat = (p_sore_throat_given_strep * p_strep) / p_sore_throat

print("Step Throat Diagnosis - Bayes Theorem (Part 2)")
print()
print("Bayes Formula: P(Strep | Sore Throat) = P(Sore Throat | Strep) × P(Strep) / P(Sore Throat)")
print()
print("P(Sore Throat)              =", round(p_sore_throat, 3))
print()
print("P(Strep | Sore Throat)      =", round(p_strep_given_sore_throat, 3))
print()
print(f"If a patient has a sore throat, there is a {round(p_strep_given_sore_throat*100, 1)}% chance they have Strep.")
