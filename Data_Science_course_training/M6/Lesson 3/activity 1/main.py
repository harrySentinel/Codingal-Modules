scores = [45, 67, 72, 88, 91, 95]

print("=== PART 1: Head and Tail ===")
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

print("Head:", head(scores))
print("Tail:", tail(scores))

print("\n=== PART 2: Base Case Trace ===")
def print_scores(lst):
    if len(lst) == 0:
        print("Base case reached — list is empty")
        return
    print("Score:", lst[0])
    print_scores(lst[1:])

print_scores(scores)

print("\n=== PART 3: Is Leaderboard Sorted? ===")
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return is_sorted(lst[1:])

print("Sorted?", is_sorted(scores))

print("\n=== PART 4: Sum of All Scores ===")
def total(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + total(lst[1:])

print("Total Score:", total(scores))

print("\n=== PART 5: Champion's Score (Maximum) ===")
def champion(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = champion(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

print("Champion's Score:", champion(scores))
