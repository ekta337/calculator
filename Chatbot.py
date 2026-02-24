# Enhanced Rule-Based Chatbot
import datetime
import random

print("Hello! I am SmartBot 🤖")
print("Type 'bye' anytime to exit.\n")

name = ""   # Store user's name

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "bye":
        print("SmartBot: Goodbye! Have a great day 😊")
        break

    # Greetings
    elif user_input in ["hi", "hello", "hey"]:
        print("SmartBot: Hello there! What can I do for you?")

    # Asking name
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        print(f"SmartBot: Nice to meet you, {name.title()}!")

    elif "your name" in user_input:
        print("SmartBot: My name is SmartBot, your virtual assistant.")

    # Asking time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("SmartBot: Current time is", current_time)

    # Asking date
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print("SmartBot: Today's date is", current_date)

    # Mood detection
    elif "how are you" in user_input:
        print("SmartBot: I'm functioning perfectly! Thanks for asking 😊")

    elif "sad" in user_input:
        print("SmartBot: I'm sorry to hear that. Things will get better 💙")

    elif "happy" in user_input:
        print("SmartBot: That's wonderful to hear! 😄")

    # Simple calculator
    elif "add" in user_input:
        try:
            numbers = user_input.split()
            num1 = int(numbers[-2])
            num2 = int(numbers[-1])
            print("SmartBot: The sum is", num1 + num2)
        except:
            print("SmartBot: Please enter numbers like: add 5 10")

    # Random joke
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the computer cold? It forgot to close Windows!"
        ]
        print("SmartBot:", random.choice(jokes))

    # Help menu
    elif "help" in user_input:
        print("SmartBot: I can do the following:")
        print("- Greet you")
        print("- Tell time/date")
        print("- Remember your name")
        print("- Add two numbers (example: add 5 10)")
        print("- Tell jokes")
        print("- Respond to your mood")

    # If name is known, personalize response
    elif name != "":
        print(f"SmartBot: {name.title()}, I am not sure I understand. Try typing 'help'.")

    # Default response
    else:
        print("SmartBot: Sorry, I didn't understand that. Type 'help' to see what I can do.")
