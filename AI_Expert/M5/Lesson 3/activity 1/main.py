import requests
import numpy as np
from PIL import Image, ImageFilter
from io import BytesIO
from config import API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-inpainting"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def restore_scratched(image_path):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    scratched = img_array.copy()
    for i in range(5):
        x = np.random.randint(0, img_array.shape[1] - 20)
        y = np.random.randint(0, img_array.shape[0])
        scratched[y:y+3, x:x+20] = [255, 255, 255]

    scratched_img = Image.fromarray(scratched)
    scratched_img.save("scratched.png")
    scratched_img.show()
    print("Scratched version saved as 'scratched.png'")

    restored = scratched_img.filter(ImageFilter.MedianFilter(size=3))
    restored.save("restored.png")
    restored.show()
    print("Restored version saved as 'restored.png'")

def inpaint_with_ai(image_path, prompt):
    img = Image.open(image_path).convert("RGB").resize((512, 512))
    mask = Image.new("RGB", (512, 512), (0, 0, 0))
    mask_array = np.array(mask)
    mask_array[200:300, 200:300] = [255, 255, 255]
    mask_img = Image.fromarray(mask_array)

    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")

    mask_bytes = BytesIO()
    mask_img.save(mask_bytes, format="PNG")

    files = {
        "inputs": img_bytes.getvalue(),
        "mask": mask_bytes.getvalue(),
    }
    data = {"prompt": prompt}

    print("Sending to AI for inpainting...")
    response = requests.post(API_URL, headers=headers, files=files, data=data)
    if response.status_code == 200:
        result = Image.open(BytesIO(response.content))
        result.save("inpainted.png")
        result.show()
        print("Inpainted image saved as 'inpainted.png'")
    else:
        print(f"Error {response.status_code}: {response.text}")

print("=== Inpainting and Restoration Challenge ===\n")
print("1. Restore scratched image (local)")
print("2. AI Inpainting (HuggingFace)")
choice = input("\nChoice (1/2): ").strip()

if choice == "1":
    path = input("Image path: ").strip()
    restore_scratched(path)
elif choice == "2":
    path = input("Image path: ").strip()
    prompt = input("Describe what should fill the masked region: ").strip()
    inpaint_with_ai(path, prompt)
else:
    print("Invalid choice.")
