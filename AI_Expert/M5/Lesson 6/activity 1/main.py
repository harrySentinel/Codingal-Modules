import requests
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import os
from config import API_TOKEN

TROCR_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-large-printed"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def preprocess(image_path):
    img = Image.open(image_path).convert("L")
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)
    preprocessed_path = "preprocessed.png"
    img.save(preprocessed_path)
    return preprocessed_path

def ocr_tesseract(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img).strip()

def ocr_trocr(path):
    with open(path, "rb") as f:
        data = f.read()
    print("Sending to TrOCR (HuggingFace)...")
    response = requests.post(TROCR_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        print(f"TrOCR Error {response.status_code}: {response.text}")
        return None

def compare_results(path):
    print("\n--- Tesseract OCR ---")
    t_text = ocr_tesseract(path)
    print(t_text if t_text else "(no text detected)")

    print("\n--- TrOCR (AI Model) ---")
    ai_text = ocr_trocr(path)
    print(ai_text if ai_text else "(no text detected)")

    return t_text, ai_text

print("=== AI-Powered Image-to-Text: Part 2 ===\n")
print("1. Basic OCR (Tesseract)")
print("2. AI OCR (TrOCR via HuggingFace)")
print("3. Compare both + preprocess")
choice = input("\nChoice (1/2/3): ").strip()

path = input("Image path: ").strip()
if not os.path.exists(path):
    print("File not found."); exit()

if choice == "1":
    text = ocr_tesseract(path)
    print(f"\nExtracted:\n{text}")

elif choice == "2":
    text = ocr_trocr(path)
    print(f"\nExtracted:\n{text}")

elif choice == "3":
    print("\nPreprocessing image...")
    clean_path = preprocess(path)
    print("Comparing results on preprocessed image...\n")
    t_text, ai_text = compare_results(clean_path)

    save = input("\nSave both results? (yes/no): ").strip().lower()
    if save == "yes":
        with open("comparison.txt", "w") as f:
            f.write(f"Tesseract:\n{t_text}\n\nTrOCR:\n{ai_text}")
        print("Saved to 'comparison.txt'")
else:
    print("Invalid choice.")
