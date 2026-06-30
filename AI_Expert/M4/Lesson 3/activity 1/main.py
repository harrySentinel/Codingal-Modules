import requests
import random

print("=== Random Facts Explorer ===\n")

def get_random_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url, params={"language": "en"})
    if response.status_code == 200:
        return response.json()["text"]
    return None

def get_cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        return response.json()["fact"]
    return None

def get_number_fact(number):
    response = requests.get(f"http://numbersapi.com/{number}/trivia")
    if response.status_code == 200:
        return response.text
    return None

def get_activity():
    response = requests.get("https://www.boredapi.com/api/activity")
    if response.status_code == 200:
        data = response.json()
        return f"{data['activity']} (Type: {data['type']}, Participants: {data['participants']})"
    return None

while True:
    print("\nWhat would you like?")
    print("1. Random Fun Fact")
    print("2. Cat Fact")
    print("3. Number Fact")
    print("4. Random Activity Idea")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
        fact = get_random_fact()
        print(f"\nFact: {fact}" if fact else "Could not fetch fact.")
    elif choice == "2":
        fact = get_cat_fact()
        print(f"\nCat Fact: {fact}" if fact else "Could not fetch cat fact.")
    elif choice == "3":
        num = input("Enter a number: ").strip()
        fact = get_number_fact(num) if num.isdigit() else None
        print(f"\n{fact}" if fact else "Invalid number or could not fetch.")
    elif choice == "4":
        activity = get_activity()
        print(f"\nActivity: {activity}" if activity else "Could not fetch activity.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
