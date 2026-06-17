import random

bag = ['Red', 'Red', 'Red', 'Blue', 'Blue', 'Green']

print("Bag contains:", bag)
print("Total balls:", len(bag))
print()

picked = random.choice(bag)
print("Randomly picked ball:", picked)
print()

red_count = bag.count('Red')
blue_count = bag.count('Blue')
green_count = bag.count('Green')
total = len(bag)

print("Probability of Red  =", red_count, "/", total, "=", round(red_count/total, 2))
print("Probability of Blue =", blue_count, "/", total, "=", round(blue_count/total, 2))
print("Probability of Green=", green_count, "/", total, "=", round(green_count/total, 2))
