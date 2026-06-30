import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            text = r.recognize_google(audio).lower()
            print(f"You: {text}")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, I need internet for speech recognition.")
            return ""

def respond(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "joke" in command:
        speak("Why don't scientists trust atoms? Because they make up everything!")

    elif "your name" in command:
        speak("I am your offline voice assistant.")

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "bye" in command or "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day!")
        return False

    else:
        speak("I didn't understand that. Try asking about time, date, or say open YouTube.")

    return True

speak("Voice Assistant is ready. Say hello to get started!")

running = True
while running:
    command = listen()
    if command:
        running = respond(command)
