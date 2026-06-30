import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ask(prompt, temperature=0.7, instruction=None):
    full_prompt = f"{instruction}\n\n{prompt}" if instruction else prompt
    model = genai.GenerativeModel(
        "gemini-pro",
        generation_config=genai.types.GenerationConfig(temperature=temperature)
    )
    return model.generate_content(full_prompt).text

print("=== Advanced Prompt Engineering: Temperature & Instructions ===\n")

topic = "Write a short story about a robot."

print("--- Temperature Demo ---")
print(f"Prompt: '{topic}'\n")

for temp in [0.0, 0.5, 1.0]:
    print(f"Temperature = {temp}")
    resp = ask(topic, temperature=temp)
    print(resp[:250])
    print()

print("--- Instruction-Based Prompts ---\n")

instructions = [
    "You are a formal academic writer. Use professional language.",
    "You are a fun children's story author. Use simple words and humor.",
    "You are a news reporter. Write in a factual, concise style.",
]

base = "Explain how the internet works."

for inst in instructions:
    print(f"Instruction: {inst}")
    resp = ask(base, temperature=0.7, instruction=inst)
    print(f"Response:\n{resp[:300]}\n")

print("=== Try It Yourself ===")
inst = input("Enter an instruction (e.g. 'You are a pirate'): ").strip()
prompt = input("Enter your prompt: ").strip()
temp = input("Temperature (0.0 to 1.0, default 0.7): ").strip()
temp = float(temp) if temp else 0.7

print(f"\nGemini says:\n{ask(prompt, temperature=temp, instruction=inst)}")
