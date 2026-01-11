# Simple Rule-Based Chatbot

print("ChatBot: Hello! I am a simple chatbot.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi!")

    elif user_input == "how are you":
        print("Bot: I am fine, thank you!")

    elif user_input == "what is your name":
        print("Bot: My name is chatBot")

    elif user_input == "you’re a genius" or user_input == "you're a genius":
        print("Bot: Thank you! I’m designed to help you as best as I can.")

    elif user_input == "how much do you sleep":
        print("Bot: Well, I never sleep and do not have baggy eyes and I am always available whenever you need help.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
