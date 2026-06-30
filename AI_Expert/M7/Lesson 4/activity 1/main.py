import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def ask_with_role(role, prompt, feedback=None):
    base = f"You are {role}.\n\n{prompt}"
    if feedback:
        base += f"\n\nPrevious response feedback: {feedback}\nPlease improve your response based on this feedback."
    return model.generate_content(base).text

ROLES = {
    "1": ("a strict teacher",         "Explain photosynthesis to a student who got it wrong in an exam."),
    "2": ("a friendly tutor",          "Explain photosynthesis in a fun, simple way for a beginner."),
    "3": ("a scientist",               "Explain photosynthesis using technical and precise language."),
    "4": ("a motivational coach",      "Motivate a student who is struggling to understand photosynthesis."),
    "5": ("a storyteller",             "Explain photosynthesis through a short creative story."),
}

print("=== Reinforcement Learning & Role-Based Prompts ===\n")
print("Role-Based Prompting: Same topic, different roles.\n")

for k, (role, prompt) in ROLES.items():
    print(f"{k}. Role: {role}")

choice = input("\nPick a role (1-5): ").strip()
if choice not in ROLES:
    choice = "1"

role, prompt = ROLES[choice]
print(f"\nRole: {role}")
print(f"Prompt: {prompt}\n")

response = ask_with_role(role, prompt)
print(f"Response:\n{response}\n")

print("--- Reinforcement Loop (give feedback to improve) ---")
for i in range(2):
    fb = input(f"Feedback round {i+1} (or press Enter to skip): ").strip()
    if not fb:
        break
    response = ask_with_role(role, prompt, feedback=fb)
    print(f"\nImproved Response:\n{response}\n")

print("=== Custom Role Prompt ===")
custom_role = input("Define your role (e.g. 'a pirate captain'): ").strip()
custom_prompt = input("Enter your prompt: ").strip()
print(f"\n{ask_with_role(custom_role, custom_prompt)}")
