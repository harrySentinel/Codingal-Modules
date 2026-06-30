import speech_recognition as sr

r = sr.Recognizer()

def listen_and_transcribe():
    with sr.Microphone() as source:
        print("Listening... (speak now)")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=7, phrase_time_limit=10)
            return audio
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

def transcribe(audio, engine="google"):
    try:
        if engine == "google":
            return r.recognize_google(audio)
        elif engine == "sphinx":
            return r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[API Error: {e}]"

print("=== Speech to Text ===\n")
print("Engines: 1. Google (online)  2. Sphinx (offline)")
choice = input("Choose engine (1/2): ").strip()
engine = "google" if choice == "1" else "sphinx"

history = []

while True:
    cmd = input("\nPress Enter to speak (or type 'quit' to exit, 'history' to see all): ").strip().lower()
    if cmd == "quit":
        print("Goodbye!")
        break
    elif cmd == "history":
        if not history:
            print("No transcriptions yet.")
        else:
            for i, t in enumerate(history, 1):
                print(f"{i}. {t}")
        continue

    audio = listen_and_transcribe()
    if audio:
        text = transcribe(audio, engine)
        print(f"Transcribed: {text}")
        history.append(text)

        save = input("Save this to file? (yes/no): ").strip().lower()
        if save == "yes":
            with open("transcription.txt", "a") as f:
                f.write(text + "\n")
            print("Saved to 'transcription.txt'")
