

def generate_message(prompt: str) -> str:
    prompt = prompt.lower()
    if "diwali" in prompt:
        return "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!"
    elif "birthday" in prompt:
        return "Hello {name}, Happy Birthday! Wishing you a wonderful year ahead."
    elif "thank you" in prompt:
        return "Hello {name}, Thank you for your support and trust in us!"
    else:
        return "Hello {name}, Greetings from our team! How can we assist you today?"
