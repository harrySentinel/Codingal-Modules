import requests

print("=== Trivia & Fun Facts Bot ===\n")

def fetch_trivia(amount=5, category=None, difficulty=None):
    url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple"}
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    response = requests.get(url, params=params)
    return response.json()

def play_trivia():
    print("Categories: 9=General, 17=Science, 21=Sports, 23=History")
    cat = input("Enter category number (or press Enter to skip): ").strip()
    diff = input("Difficulty (easy/medium/hard or skip): ").strip().lower()

    category = int(cat) if cat.isdigit() else None
    difficulty = diff if diff in ["easy", "medium", "hard"] else None

    data = fetch_trivia(amount=3, category=category, difficulty=difficulty)

    if data["response_code"] != 0:
        print("Could not fetch trivia. Try again.")
        return

    score = 0
    questions = data["results"]

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        options = q["incorrect_answers"] + [q["correct_answer"]]
        import random; random.shuffle(options)
        for j, opt in enumerate(options, 1):
            print(f"  {j}. {opt}")
        ans = input("Your answer (1-4): ").strip()
        try:
            chosen = options[int(ans) - 1]
            if chosen == q["correct_answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Answer was: {q['correct_answer']}")
        except:
            print(f"Invalid input. Answer was: {q['correct_answer']}")

    print(f"\nYour Score: {score}/{len(questions)}")

play_trivia()
