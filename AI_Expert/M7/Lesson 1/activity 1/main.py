import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def ask(prompt):
    response = model.generate_content(prompt)
    return response.text

print("=== Prompt Engineering: Clarity, Specificity & Context ===\n")
print("We will compare vague vs. clear prompts and see how Gemini responds differently.\n")

examples = [
    {
        "topic": "Clarity",
        "vague":   "Tell me about dogs.",
        "clear":   "In 3 bullet points, explain what makes dogs good pets for families with children."
    },
    {
        "topic": "Specificity",
        "vague":   "Write something about climate.",
        "clear":   "Write a 2-sentence explanation of how climate change affects ocean levels, suitable for a 10-year-old."
    },
    {
        "topic": "Contextual Information",
        "vague":   "Give me advice.",
        "clear":   "I am a 16-year-old student who wants to start learning Python. Give me 3 beginner tips."
    },
]

for ex in examples:
    print(f"{'='*50}")
    print(f"Topic: {ex['topic']}")
    print(f"\nVague Prompt: {ex['vague']}")
    vague_resp = ask(ex["vague"])
    print(f"Response:\n{vague_resp[:300]}...\n")

    print(f"Clear Prompt: {ex['clear']}")
    clear_resp = ask(ex["clear"])
    print(f"Response:\n{clear_resp}\n")

print("=== Try Your Own ===")
while True:
    p = input("Enter your prompt (or 'exit'): ").strip()
    if p.lower() == "exit":
        break
    print(f"\nGemini says:\n{ask(p)}\n")
