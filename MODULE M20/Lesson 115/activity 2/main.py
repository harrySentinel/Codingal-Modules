print("Quick Draw - AI That Recognizes Doodles!")
print()
print("Google's Quick Draw is a game where you draw something")
print("and an AI tries to guess what it is in 20 seconds.")
print()
print("How it works:")
print("  1. User draws a doodle on screen")
print("  2. The drawing is converted into pixel data")
print("  3. A Neural Network analyzes the pattern")
print("  4. AI predicts the most likely object")
print()
print("It was trained on over 50 million drawings from 15 million people!")
print()

guesses = {
    "circle":   "Sun / Ball / Clock",
    "triangle": "Mountain / Pizza slice / Arrow",
    "lines":    "Ladder / Fence / Road",
    "curves":   "Snake / River / Wave"
}

print("Example AI Guesses based on shapes:")
for shape, guess in guesses.items():
    print(f"  Shape: {shape:10} -> AI guesses: {guess}")

print()
shape = input("Draw a shape (circle/triangle/lines/curves): ").strip().lower()
if shape in guesses:
    print("AI thinks it could be:", guesses[shape])
else:
    print("Interesting drawing! The AI is still learning.")
