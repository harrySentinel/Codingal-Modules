import requests
from config import API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def summarize(text, max_length=130, min_length=30):
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_length,
            "min_length": min_length,
            "do_sample": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    if isinstance(result, list):
        return result[0]["summary_text"]
    return None

print("=== LLM Text Summarization Tool ===\n")

sample = """
Artificial intelligence is transforming industries across the globe. From healthcare to finance,
AI systems are being used to automate tasks, analyze massive datasets, and generate insights
that were previously impossible to obtain. Machine learning models can now diagnose diseases
from medical images, predict stock market trends, and even write code. However, with this rapid
advancement comes a set of ethical challenges including bias in algorithms, job displacement,
and concerns about data privacy. Researchers and policymakers are now working together to
create frameworks that ensure AI development remains responsible and beneficial to society.
"""

print("Original Text:")
print(sample.strip())
print(f"\nWord Count: {len(sample.split())}")

print("\nGenerating summary...")
summary = summarize(sample)

if summary:
    print(f"\nSummary:\n{summary}")
    print(f"\nSummary Word Count: {len(summary.split())}")
else:
    print("Could not generate summary.")

print("\n--- Try Your Own Text ---")
while True:
    user_text = input("\nPaste your text (or type 'exit'): ").strip()
    if user_text.lower() == "exit":
        print("Goodbye!")
        break
    if len(user_text.split()) < 30:
        print("Text too short. Please enter at least 30 words.")
        continue
    result = summarize(user_text)
    print(f"\nSummary: {result}" if result else "Could not summarize.")
