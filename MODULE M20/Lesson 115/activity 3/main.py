translations = {
    "en": {
        "hello": {"hi": "hola", "es": "hola", "fr": "bonjour", "de": "hallo", "ja": "konnichiwa"},
        "thank you": {"hi": "dhanyavaad", "es": "gracias", "fr": "merci", "de": "danke", "ja": "arigatou"},
        "good morning": {"hi": "suprabhat", "es": "buenos dias", "fr": "bonjour", "de": "guten morgen", "ja": "ohayou"},
        "goodbye": {"hi": "alvida", "es": "adios", "fr": "au revoir", "de": "tschuss", "ja": "sayonara"},
        "my name is aditya": {"hi": "mera naam aditya hai", "es": "mi nombre es aditya", "fr": "je m'appelle aditya"}
    }
}

lang_names = {"hi": "Hindi", "es": "Spanish", "fr": "French", "de": "German", "ja": "Japanese"}

print("Things Translator - AI Language Translator")
print()
print("Available phrases:")
for phrase in translations["en"]:
    print(" -", phrase)
print()
print("Available languages:", ", ".join([f"{k} ({v})" for k, v in lang_names.items()]))
print()

phrase = input("Enter a phrase to translate: ").strip().lower()
lang = input("Enter target language code (hi/es/fr/de/ja): ").strip().lower()

if phrase in translations["en"] and lang in translations["en"].get(phrase, {}):
    print(f"\nTranslation in {lang_names.get(lang, lang)}: {translations['en'][phrase][lang]}")
else:
    print("Translation not available. AI is still learning new phrases!")
