import random
from datetime import datetime

def chatbot():
    print("Chatbot: Hi there! I'm your friendly chatbot. Ask me anything, and I'll do my best to help!")
    print("Type 'exit' anytime to leave the chat.\n")

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get if you cross a snowman and a dog? Frostbite.",
        "Why did the computer visit the doctor? It caught a virus!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call fake spaghetti? An impasta!"
    ]

    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Life is what happens when you’re busy making other plans. - John Lennon"
    ]

    countries = {
        "france": "The capital of France is Paris.",
        "germany": "The capital of Germany is Berlin.",
        "japan": "The capital of Japan is Tokyo.",
        "india": "The capital of India is New Delhi.",
        "canada": "The capital of Canada is Ottawa.",
        "italy": "The capital of Italy is Rome.",
        "brazil": "The capital of Brazil is Brasília.",
        "australia": "The capital of Australia is Canberra.",
        "china": "The capital of China is Beijing.",
        "russia": "The capital of Russia is Moscow."
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["exit", "bye", "quit"]:
            print("Chatbot: Goodbye! Take care!")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you today?")

        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")

        elif "date" in user_input:
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.")

        elif "joke" in user_input:
            print(f"Chatbot: Here's a joke for you: {random.choice(jokes)}")

        elif "quote" in user_input:
            print(f"Chatbot: Here's an inspirational quote: {random.choice(quotes)}")

        elif "capital of" in user_input:
            country = user_input.split("capital of")[-1].strip()
            response = countries.get(country, f"Sorry, I don't know the capital of {country}.")
            print(f"Chatbot: {response}")

        elif "calculate" in user_input:
            print("Chatbot: Please enter a mathematical expression (e.g., 12 + 7):")
            expression = input("You: ")
            try:
                result = eval(expression)
                print(f"Chatbot: The result is {result}.")
            except Exception:
                print("Chatbot: Oops! That doesn't look like a valid math expression.")

        elif "weather" in user_input:
            print("Chatbot: I'm not connected to live weather data, but it's always a good idea to carry an umbrella just in case!")

        elif "hobby" in user_input or "hobbies" in user_input:
            print("Chatbot: My hobbies include chatting with you, making jokes, and learning new things!")

        elif "tell me about" in user_input:
            if "python" in user_input:
                print("Chatbot: Python is a powerful, easy-to-learn programming language used for a variety of applications.")
            elif "ai" in user_input or "artificial intelligence" in user_input:
                print("Chatbot: AI is the simulation of human intelligence in machines capable of performing tasks like learning and problem-solving.")
            elif "space" in user_input:
                print("Chatbot: Space is a vast expanse beyond Earth's atmosphere, full of stars, planets, and other celestial objects!")
            else:
                print("Chatbot: That's an interesting topic! Unfortunately, I don't have information on that right now.")

        elif "thank you" in user_input:
            print("Chatbot: You're welcome! I'm always here to help.")

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you try asking in a different way?")

chatbot()
