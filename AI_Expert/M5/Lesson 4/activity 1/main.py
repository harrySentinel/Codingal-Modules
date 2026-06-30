import requests
from PIL import Image
from io import BytesIO
from config import API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def describe_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    print("Sending image to AI for description...")
    response = requests.post(API_URL, headers=headers, data=data)
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def describe_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Could not fetch image from URL.")
        return None
    data = response.content
    api_response = requests.post(API_URL, headers=headers, data=data)
    if api_response.status_code == 200:
        return api_response.json()[0]["generated_text"]
    else:
        print(f"Error {api_response.status_code}: {api_response.text}")
        return None

print("=== AI-Powered Image Description ===\n")
print("1. Describe a local image")
print("2. Describe image from URL")
choice = input("\nChoice (1/2): ").strip()

if choice == "1":
    path = input("Image path: ").strip()
    caption = describe_image(path)
    if caption:
        print(f"\nAI Description: {caption}")
elif choice == "2":
    url = input("Image URL: ").strip()
    caption = describe_from_url(url)
    if caption:
        print(f"\nAI Description: {caption}")
else:
    print("Invalid choice.")

if caption:
    save = input("\nSave description to file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("description.txt", "w") as f:
            f.write(caption)
        print("Saved to 'description.txt'")
