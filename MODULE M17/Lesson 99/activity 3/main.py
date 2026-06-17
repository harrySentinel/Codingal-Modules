shirts = ['Red', 'Blue', 'Green', 'White', 'Black']
pants = ['Jeans', 'Trousers', 'Shorts']

total_outfits = len(shirts) * len(pants)

print("Shirts available:", shirts)
print("Pants available: ", pants)
print()
print("Total outfit combinations:", total_outfits)
print()

p_red_shirt = 1 / len(shirts)
p_jeans = 1 / len(pants)
p_red_and_jeans = p_red_shirt * p_jeans

print("P(Red Shirt)          =", round(p_red_shirt, 2))
print("P(Jeans)              =", round(p_jeans, 2))
print("P(Red Shirt & Jeans)  =", round(p_red_and_jeans, 2))
print()

for shirt in shirts:
    for pant in pants:
        print(f"  {shirt} + {pant}")
