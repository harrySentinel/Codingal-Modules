import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def ask(prompt):
    return model.generate_content(prompt).text

task = "Classify the sentiment of this sentence as Positive, Negative, or Neutral."
sentence = "The movie was absolutely fantastic!"

print("=== Zero-Shot, One-Shot, and Few-Shot Learning ===\n")

print("--- Zero-Shot ---")
zero_shot = f"{task}\n\nSentence: {sentence}"
print(f"Prompt:\n{zero_shot}\n")
print(f"Response: {ask(zero_shot)}\n")

print("--- One-Shot ---")
one_shot = f"""{task}

Example:
Sentence: "I love this product!" → Positive

Now classify:
Sentence: "{sentence}" →"""
print(f"Prompt:\n{one_shot}\n")
print(f"Response: {ask(one_shot)}\n")

print("--- Few-Shot ---")
few_shot = f"""{task}

Examples:
Sentence: "I love this product!" → Positive
Sentence: "This is the worst service ever." → Negative
Sentence: "The package arrived on time." → Neutral

Now classify:
Sentence: "{sentence}" →"""
print(f"Prompt:\n{few_shot}\n")
print(f"Response: {ask(few_shot)}\n")

print("=== Try Your Own Sentence ===")
while True:
    s = input("Enter a sentence (or 'exit'): ").strip()
    if s.lower() == "exit":
        break
    prompt = f"""{task}

Examples:
Sentence: "I love this product!" → Positive
Sentence: "This is the worst service ever." → Negative
Sentence: "The package arrived on time." → Neutral

Now classify:
Sentence: "{s}" →"""
    print(f"Sentiment: {ask(prompt)}\n")
