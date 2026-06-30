keypad = {
    "2": "abc", "3": "def", "4": "ghi",
    "5": "jkl", "6": "mno", "7": "pqrs",
    "8": "tuv", "9": "wxyz"
}

def combinations(digits, current=""):
    if len(digits) == 0:
        print(current)
        return
    for letter in keypad[digits[0]]:
        combinations(digits[1:], current + letter)

digits = input("Enter digits (e.g. 23): ")
print(f"\nAll combinations for '{digits}':\n")
combinations(digits)
