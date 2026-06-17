print("Welcome to Codingal's Jarvis - An Intelligent Assistant")
print()

training_data = {
    "hello": "Hi there! I am Jarvis, your AI assistant.",
    "what is machine learning": "Machine Learning is teaching computers to learn from data without being explicitly programmed.",
    "what is ai": "AI stands for Artificial Intelligence - making machines think and act like humans.",
    "who created you": "I was created by Aditya Srivastava at Codingal!",
    "what can you do": "I can answer your questions, help you learn, and assist with coding!",
    "bye": "Goodbye! Keep learning and keep coding!"
}

print("Jarvis is ready. Type 'bye' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ").strip().lower()
    if user_input in training_data:
        print("Jarvis:", training_data[user_input])
    else:
        print("Jarvis: I am still learning. I don't know the answer to that yet!")
    if user_input == "bye":
        break
