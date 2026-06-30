import requests

print("=== Getting Started with APIs ===\n")

url = "https://catfact.ninja/fact"

response = requests.get(url)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"Response Data: {data}")
    print(f"\nFact: {data['fact']}")
else:
    print("Failed to fetch data.")

print("\n--- Request Headers ---")
print(f"Content-Type: {response.headers['Content-Type']}")

print("\n--- Passing Parameters ---")
url2 = "https://catfact.ninja/facts"
params = {"limit": 3}
response2 = requests.get(url2, params=params)

if response2.status_code == 200:
    facts = response2.json()["data"]
    for i, item in enumerate(facts, 1):
        print(f"{i}. {item['fact']}")
