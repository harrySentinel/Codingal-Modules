import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

engine = pyttsx3.init()
engine.setProperty("rate", 150)

LANGUAGES = {
    "1": ("Hindi",    "hi"),
    "2": ("French",   "fr"),
    "3": ("Spanish",  "es"),
    "4": ("German",   "de"),
    "5": ("Japanese", "ja"),
    "6": ("Arabic",   "ar"),
    "7": ("Chinese",  "zh-CN"),
}

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=10)
            return r.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Could not understand.")
            return None
        except sr.RequestError as e:
            print(f"API error: {e}")
            return None

def translate(text, target_lang):
    return GoogleTranslator(source="auto", target=target_lang).translate(text)

print("=== Real-Time Speech Translation ===\n")
print("Available target languages:")
for k, (name, code) in LANGUAGES.items():
    print(f"  {k}. {name} ({code})")

choice = input("\nChoose target language (1-7): ").strip()
if choice not in LANGUAGES:
    print("Invalid choice. Defaulting to Hindi.")
    choice = "1"

lang_name, lang_code = LANGUAGES[choice]
print(f"\nTranslating speech to: {lang_name}\n")
print("Press Enter to start listening. Type 'exit' to quit.\n")

while True:
    cmd = input("Press Enter to speak (or 'exit'): ").strip().lower()
    if cmd == "exit":
        print("Goodbye!")
        break

    original = listen()
    if not original:
        continue

    print(f"\nOriginal ({original})")

    translated = translate(original, lang_code)
    print(f"Translated ({lang_name}): {translated}\n")

    speak(translated)
