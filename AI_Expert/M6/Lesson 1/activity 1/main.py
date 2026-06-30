import speech_recognition as sr

print("=== Hello AI, Can You Hear Me? ===\n")

r = sr.Recognizer()

print("Available microphones:")
for i, mic in enumerate(sr.Microphone.list_microphone_names()):
    print(f"  {i}: {mic}")

print("\nUsing default microphone...\n")

with sr.Microphone() as source:
    print("Adjusting for background noise... please wait.")
    r.adjust_for_ambient_noise(source, duration=2)
    print(f"Energy threshold set to: {r.energy_threshold:.2f}")

    print("\nSay something!")
    try:
        audio = r.listen(source, timeout=5)
        print("Got it! Recognizing...")
        text = r.recognize_google(audio)
        print(f"\nYou said: '{text}'")
    except sr.WaitTimeoutError:
        print("No speech detected within 5 seconds.")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API error: {e}")

print("\nMicrophone test complete!")
