# Simple Rule-Based Chatbot

def chatbot():
    print("Hello! I am your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("Bot: I'm a simple chatbot built with Python.")
        
        elif "help" in user_input:
            print("Bot: Sure! You can ask me about my name, say hello, or ask how I am.")
        
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        
        else:
            print("Bot: Sorry, I don't understand that. Try asking something else.")

if __name__ == "__main__":
    chatbot()
