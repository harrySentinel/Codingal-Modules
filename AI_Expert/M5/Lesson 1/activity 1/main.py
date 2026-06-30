import requests
from PIL import Image
from io import BytesIO
from config import API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_image(prompt, filename="output.png"):
    print(f"Generating image for: '{prompt}'...")
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(filename)
        image.show()
        print(f"Image saved as '{filename}'")
    else:
        print(f"Error {response.status_code}: {response.text}")

print("=== Text-to-Image Generation ===\n")
print("Type a description and AI will generate an image.")
print("Type 'exit' to quit.\n")

count = 1
while True:
    prompt = input("Your prompt: ").strip()
    if prompt.lower() == "exit":
        print("Goodbye!")
        break
    if not prompt:
        print("Please enter a prompt.")
        continue
    generate_image(prompt, filename=f"generated_{count}.png")
    count += 1
