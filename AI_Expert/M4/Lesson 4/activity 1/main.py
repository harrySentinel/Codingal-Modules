import requests
from config import API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def classify_text(text, labels):
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": labels}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

print("=== NLP Text Classification with Hugging Face ===\n")

labels = ["technology", "sports", "politics", "entertainment", "science"]

samples = [
    "NASA launched a new rocket to explore Mars.",
    "The football team won the championship last night.",
    "The new iPhone has a better camera and faster processor.",
    "The president signed a new climate change policy.",
    "The movie broke all box office records this weekend."
]

for text in samples:
    result = classify_text(text, labels)
    top_label = result["labels"][0]
    top_score = result["scores"][0]
    print(f"Text: {text}")
    print(f"Category: {top_label} ({top_score:.2%})\n")

print("--- Custom Input ---")
user_text = input("Enter your own sentence to classify: ")
result = classify_text(user_text, labels)
for label, score in zip(result["labels"], result["scores"]):
    print(f"  {label}: {score:.2%}")
