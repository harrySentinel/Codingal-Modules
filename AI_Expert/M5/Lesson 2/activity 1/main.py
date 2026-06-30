from PIL import Image, ImageEnhance, ImageFilter
import os

def load_image(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None
    return Image.open(path)

def enhance_brightness(img, factor):
    return ImageEnhance.Brightness(img).enhance(factor)

def enhance_contrast(img, factor):
    return ImageEnhance.Contrast(img).enhance(factor)

def enhance_sharpness(img, factor):
    return ImageEnhance.Sharpness(img).enhance(factor)

def apply_blur(img):
    return img.filter(ImageFilter.GaussianBlur(radius=2))

def apply_sharpen(img):
    return img.filter(ImageFilter.SHARPEN)

def apply_edge(img):
    return img.filter(ImageFilter.FIND_EDGES)

def apply_emboss(img):
    return img.filter(ImageFilter.EMBOSS)

print("=== Post-Processing Magic Workshop ===\n")
path = input("Enter image path (e.g. generated_1.png): ").strip()
img = load_image(path)
if not img:
    exit()

img.show()
print(f"Image loaded: {img.size[0]}x{img.size[1]} px\n")

while True:
    print("Options:")
    print("1. Brightness  2. Contrast  3. Sharpness")
    print("4. Blur        5. Sharpen   6. Edge Detect")
    print("7. Emboss      8. Save      9. Exit")
    choice = input("\nChoice: ").strip()

    if choice == "1":
        f = float(input("Factor (0.5=darker, 2.0=brighter): "))
        img = enhance_brightness(img, f)
        img.show()
    elif choice == "2":
        f = float(input("Factor (0.5=less, 2.0=more): "))
        img = enhance_contrast(img, f)
        img.show()
    elif choice == "3":
        f = float(input("Factor (0.5=blurry, 2.0=sharp): "))
        img = enhance_sharpness(img, f)
        img.show()
    elif choice == "4":
        img = apply_blur(img)
        img.show()
    elif choice == "5":
        img = apply_sharpen(img)
        img.show()
    elif choice == "6":
        img = apply_edge(img)
        img.show()
    elif choice == "7":
        img = apply_emboss(img)
        img.show()
    elif choice == "8":
        out = input("Save as (e.g. enhanced.png): ").strip()
        img.save(out)
        print(f"Saved as '{out}'")
    elif choice == "9":
        print("Done!")
        break
    else:
        print("Invalid choice.")
