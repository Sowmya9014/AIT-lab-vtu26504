# Simple Python Chatbot

import random

# Greeting responses
greetings = ["hi", "hello", "hey", "hola", "greetings"]
responses = ["Hello there!", "Hi! How can I help you?", "Hey! What's up?", "Hi! Nice to see you."]

# Some basic Q&A
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in greetings:
        return random.choice(responses)

    elif "your name" in user_input:
        return "I'm ChatBot, your virtual assistant."

    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"

    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "date" in user_input:
        from datetime import date
        return f"Today's date is {date.today()}"

    else:
        return "I'm not sure I understand. Could you rephrase that?"

# Main chat loop
def chat():
    print("ChatBot: Hello! Type 'bye' or 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBot:", response)
        if user_input.lower() in ["bye", "exit"]:
            break

# Run the chatbot
if __name__ == "__main__":
    chat()
