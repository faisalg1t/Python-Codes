"""
Code Name : Mini Chatbot
Author : Shah Faisal
GitHub : @faisalg1t
"""

print("🤖 Bot: Hello! Type 'bye' to exit.")

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("🤖 Bot: Hey! 👋")
    elif message == "how are you":
        print("🤖 Bot: I'm doing great! 😎")
    elif message == "your name":
        print("🤖 Bot: I'm PythonBot 🐍")
    elif message == "bye":
        print("🤖 Bot: See you later! 👋")
        break
    else:
        print("🤖 Bot: Hmm... I don't understand that.")
