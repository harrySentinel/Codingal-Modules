import pytesseract
from PIL import Image
import os

print("=== AI-Powered Image-to-Text Conversion: Part 1 ===\n")
print("This tool extracts text from images using OCR (Optical Character Recognition).\n")

def extract_text(image_path):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None
    img = Image.open(image_path)
    print(f"Image loaded: {img.size[0]}x{img.size[1]} px")
    text = pytesseract.image_to_string(img)
    return text.strip()

def extract_with_details(image_path):
    img = Image.open(image_path)
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    words = [w for w in data["text"] if w.strip()]
    confidences = [data["conf"][i] for i, w in enumerate(data["text"]) if w.strip()]
    return words, confidences

path = input("Enter image path (e.g. scan.png): ").strip()
text = extract_text(path)

if text:
    print(f"\nExtracted Text:\n{'-'*40}\n{text}\n{'-'*40}")
    print(f"\nTotal characters: {len(text)}")
    print(f"Total words: {len(text.split())}")

    detail = input("\nShow word-level confidence scores? (yes/no): ").strip().lower()
    if detail == "yes":
        words, confs = extract_with_details(path)
        print("\nWord Confidence Scores:")
        for word, conf in zip(words[:20], confs[:20]):
            print(f"  '{word}' — {conf}%")

    save = input("\nSave extracted text? (yes/no): ").strip().lower()
    if save == "yes":
        with open("extracted.txt", "w") as f:
            f.write(text)
        print("Saved to 'extracted.txt'")
