import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 150)
lock = threading.Lock()

WAKE_WORD = "jarvis"

def speak(text):
    print(f"Assistant: {text}")
    with lock:
        engine.say(text)
        engine.runAndWait()

def listen(timeout=5, phrase_limit=6):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            return r.recognize_google(audio).lower()
        except:
            return ""

def handle_command(command):
    if "time" in command:
        speak(datetime.datetime.now().strftime("It is %I:%M %p"))
    elif "date" in command:
        speak(datetime.datetime.now().strftime("Today is %B %d, %Y"))
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "search" in command:
        q = command.replace("search", "").strip()
        speak(f"Searching {q}")
        webbrowser.open(f"https://www.google.com/search?q={q}")
    elif "joke" in command:
        speak("I told a joke about UDP once. I don't know if anyone got it.")
    elif "weather" in command:
        speak("I am offline. Please check a weather website.")
    elif "stop" in command or "goodbye" in command:
        speak("Shutting down. Goodbye!")
        return False
    else:
        speak("I am not sure how to help with that.")
    return True

print(f"=== Voice-Activated Assistant ===")
print(f"Say '{WAKE_WORD.upper()}' to activate.\n")

active = True
while active:
    print("Waiting for wake word...")
    heard = listen(timeout=10, phrase_limit=3)

    if WAKE_WORD in heard:
        speak("Yes? How can I help?")
        command = listen(timeout=6, phrase_limit=8)
        if command:
            active = handle_command(command)
        else:
            speak("I didn't catch that.")
