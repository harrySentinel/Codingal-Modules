import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def ask(prompt):
    return model.generate_content(prompt).text

def generate_essay(topic, tone, length):
    prompt = f"""Write a {length}-word essay about '{topic}'.
Tone: {tone}.
Structure: Introduction, 2-3 body paragraphs, Conclusion.
Do not include any headers or labels."""
    return ask(prompt)

def refine_essay(essay, instruction):
    prompt = f"""Here is an essay:

{essay}

Refine it based on this instruction: {instruction}
Return only the refined essay."""
    return ask(prompt)

def summarize_essay(essay):
    return ask(f"Summarize this essay in 2-3 sentences:\n\n{essay}")

def check_grammar(essay):
    return ask(f"List grammar and spelling mistakes in this essay and suggest corrections:\n\n{essay}")

print("=== AI Writing Assistant with Gemini ===\n")

topic = input("Essay topic: ").strip()
print("Tones: formal / casual / persuasive / academic")
tone = input("Tone: ").strip() or "formal"
print("Lengths: short (150) / medium (300) / long (500)")
length_choice = input("Length: ").strip().lower()
length = {"short": 150, "medium": 300, "long": 500}.get(length_choice, 300)

print("\nGenerating essay...\n")
essay = generate_essay(topic, tone, length)
print(f"{'='*50}\n{essay}\n{'='*50}\n")

while True:
    print("Options:")
    print("1. Refine essay  2. Summarize  3. Grammar check  4. Save  5. Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        inst = input("Refinement instruction (e.g. 'make it more formal'): ").strip()
        essay = refine_essay(essay, inst)
        print(f"\nRefined Essay:\n{essay}\n")

    elif choice == "2":
        summary = summarize_essay(essay)
        print(f"\nSummary:\n{summary}\n")

    elif choice == "3":
        feedback = check_grammar(essay)
        print(f"\nGrammar Feedback:\n{feedback}\n")

    elif choice == "4":
        fname = input("Save as (e.g. essay.txt): ").strip() or "essay.txt"
        with open(fname, "w") as f:
            f.write(essay)
        print(f"Saved to '{fname}'")

    elif choice == "5":
        print("Done!")
        break
    else:
        print("Invalid choice.")
