print("=== PART 1: Buy and Sell Stocks (Greedy) ===")
prices = [7, 1, 5, 3, 6, 4]
print("Prices:", prices)
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
print("Maximum Profit:", profit)

print("\n=== PART 2: Left Tallest Array ===")
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(heights)
left_tallest = [0] * n
left_tallest[0] = heights[0]
for i in range(1, n):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])
print("Heights:     ", heights)
print("Left Tallest:", left_tallest)

print("\n=== PART 3: Right Tallest Array ===")
right_tallest = [0] * n
right_tallest[-1] = heights[-1]
for i in range(n - 2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], heights[i])
print("Right Tallest:", right_tallest)

print("\n=== PART 4: Total Water Trapped ===")
water = 0
for i in range(n):
    w = min(left_tallest[i], right_tallest[i]) - heights[i]
    water += w
print("Total Water Trapped:", water)
