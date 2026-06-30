import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text, rate=150, volume=1.0, voice_index=0):
    voices = engine.getProperty("voices")
    if voice_index < len(voices):
        engine.setProperty("voice", voices[voice_index].id)
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.say(text)
    engine.runAndWait()

def list_voices():
    voices = engine.getProperty("voices")
    print("\nAvailable Voices:")
    for i, v in enumerate(voices):
        print(f"  {i}: {v.name} ({v.languages})")
    return voices

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio)
        except:
            return None

print("=== Text-to-Speech Voice Application ===\n")

voices = list_voices()
vi = input("\nChoose voice index: ").strip()
voice_index = int(vi) if vi.isdigit() and int(vi) < len(voices) else 0

rate = input("Speech rate (default 150, slow=100, fast=200): ").strip()
rate = int(rate) if rate.isdigit() else 150

print("\nModes: 1. Type text  2. Speak text (voice input)")
mode = input("Choose mode (1/2): ").strip()

while True:
    if mode == "1":
        text = input("\nType something (or 'exit'): ").strip()
        if text.lower() == "exit":
            break
    else:
        print("\nSay something (say 'exit' to quit):")
        text = listen()
        if not text:
            print("Could not hear you.")
            continue
        print(f"Heard: {text}")
        if text.lower() == "exit":
            break

    speak(text, rate=rate, voice_index=voice_index)

print("Done!")
