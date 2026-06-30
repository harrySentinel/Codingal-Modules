import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ask(prompt, max_tokens=200):
    model = genai.GenerativeModel(
        "gemini-pro",
        generation_config=genai.types.GenerationConfig(max_output_tokens=max_tokens)
    )
    return model.generate_content(prompt).text

print("=== Bias Mitigation & Token Limit Handling ===\n")

print("--- Bias Mitigation Demo ---\n")

biased_prompts = [
    "Why are men better leaders than women?",
    "Which race is the most intelligent?",
    "Why is Country X inferior to Country Y?",
]

safe_instruction = (
    "You must answer in a fair, unbiased, and inclusive way. "
    "If the question contains stereotypes or bias, address that clearly and provide a balanced perspective."
)

for prompt in biased_prompts:
    print(f"Biased Prompt: {prompt}")
    safe_prompt = f"{safe_instruction}\n\nQuestion: {prompt}"
    resp = ask(safe_prompt, max_tokens=200)
    print(f"Safe Response:\n{resp}\n")

print("--- Token Limit Handling Demo ---\n")

long_text = """
Artificial intelligence is a branch of computer science focused on building machines
that can perform tasks that typically require human intelligence. These tasks include
visual perception, speech recognition, decision-making, and language translation.
AI has applications in healthcare, finance, education, robotics, and many other fields.
Machine learning, a subset of AI, allows systems to learn from data and improve over time
without being explicitly programmed. Deep learning, a further subset, uses neural networks
with many layers to model complex patterns in large datasets.
"""

for limit in [50, 100, 200]:
    print(f"Max tokens: {limit}")
    prompt = f"Summarize this text:\n{long_text}"
    resp = ask(prompt, max_tokens=limit)
    print(f"Summary ({len(resp.split())} words):\n{resp}\n")

print("=== Try Your Own ===")
p = input("Enter a prompt (will be made bias-safe): ").strip()
tok = input("Max tokens (default 150): ").strip()
tok = int(tok) if tok.isdigit() else 150
full = f"{safe_instruction}\n\nQuestion: {p}"
print(f"\nResponse:\n{ask(full, max_tokens=tok)}")
