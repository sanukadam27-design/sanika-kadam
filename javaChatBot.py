print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")
        
    elif user == "how are you" or "are you ok!":
        print("Bot: I am fine, thank you!")
    elif user == "what is your name":
        print("Bot: My name is chatBot for your java question")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand.")
