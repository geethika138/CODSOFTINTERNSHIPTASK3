import re
import random

class ChatBot:
    def __init__(self):
        self.user_name = None
        self.responses = {
            "greeting": [
                "Hey there! 🌟 What’s cooking?",
                "Hello! Ready to chat? 😊",
                "Hi! What’s the latest with you?"
            ],
            "how_are_you": [
                "I'm just a bunch of code, but I'm excited to chat with you! How about you?",
                "Doing well, thanks! Just hanging out in cyberspace. How are you?"
            ],
            "name": [
                "You can call me ChatBot, your digital buddy! What about you?",
                "I'm ChatBot! What's your name, if you don't mind me asking?"
            ],
            "help": [
                "Absolutely! What can I do to brighten your day?",
                "I’m here to assist! Got something in mind?"
            ],
            "farewell": [
                "Catch you later! Don’t be a stranger! 👋",
                "Goodbye! Come back anytime for a chat! 🌈"
            ],
            "thanks": [
                "You're welcome! Anytime you need me, just holler! 🎉",
                "No problem! I’m always here for you! 😊"
            ],
            "personalization": [
                "By the way, what's your favorite color? 🎨",
                "If you could travel anywhere, where would you go? 🌍"
            ],
            "trivia": [
                "Did you know honey never spoils? It can last for thousands of years! 🍯",
                "Here's a fun fact: octopuses have three hearts! 🐙",
                "A group of flamingos is called a 'flamboyance.' How fabulous! 🦩",
                "Bananas are berries, but strawberries aren't! How weird is that? 🍌🍓"
            ],
            "jokes": [
                "Why don't scientists trust atoms? Because they make up everything! 😂",
                "What do you call fake spaghetti? An impasta! 🍝",
                "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
                "What do you call cheese that isn't yours? Nacho cheese! 🧀"
            ],
            "default": [
                "Oops! I didn’t get that. Can you say it in a different way?",
                "Hmm, I’m not sure what you mean. Let’s try again!"
            ]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        if re.search(r'\b(hello|hi|hey)\b', user_input):
            return random.choice(self.responses["greeting"])
        elif re.search(r'\b(how are you|how’s it going)\b', user_input):
            return random.choice(self.responses["how_are_you"])
        elif re.search(r'\b(your name|what is your name)\b', user_input):
            return self.handle_name_query()
        elif re.search(r'\b(help|assist)\b', user_input):
            return random.choice(self.responses["help"])
        elif re.search(r'\b(thanks|thank you)\b', user_input):
            return random.choice(self.responses["thanks"])
        elif re.search(r'\b(bored|tell me something interesting)\b', user_input):
            return random.choice(self.responses["trivia"])
        elif re.search(r'\b(joke|make me laugh)\b', user_input):
            return random.choice(self.responses["jokes"])
        elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
            return random.choice(self.responses["farewell"])

        return random.choice(self.responses["default"])

    def handle_name_query(self):
        if self.user_name:
            return f"Oh, I remember! You're {self.user_name}! 🎉 What's on your mind today?"
        else:
            self.user_name = input("What’s your name? ")
            return f"Nice to meet you, {self.user_name}! Now we can have some fun! 🎈"

def chat():
    bot = ChatBot()
    print("Chatbot: Hey! I'm ChatBot!")

    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chat()
