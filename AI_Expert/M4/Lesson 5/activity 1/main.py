import requests
from config import API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def analyze_sentiment(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    result = response.json()
    if isinstance(result, list):
        scores = result[0]
        top = max(scores, key=lambda x: x["score"])
        return top["label"], top["score"]
    return None, None

def emoji(label):
    return "😊" if label == "POSITIVE" else "😞"

print("=== Sentiment Analysis Tool ===")
print("Type a sentence to analyze. Type 'exit' to quit.\n")

history = []

while True:
    text = input("You: ").strip()
    if text.lower() == "exit":
        print("\n--- Session Summary ---")
        pos = sum(1 for l, _ in history if l == "POSITIVE")
        neg = len(history) - pos
        print(f"Total: {len(history)} | Positive: {pos} | Negative: {neg}")
        break
    if not text:
        continue

    label, score = analyze_sentiment(text)
    if label:
        print(f"Sentiment: {label} {emoji(label)} (Confidence: {score:.2%})\n")
        history.append((label, score))
    else:
        print("Could not analyze. Try again.\n")
