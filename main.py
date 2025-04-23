import datetime
import wikipedia
import pyjokes

def greet():
    print("🤖 Hello Boss! I’m your Python Chatbot. How can I help you today?")

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_info(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "Sorry Boss, I couldn't find anything."

def get_joke():
    return pyjokes.get_joke()

def mainmenu():
    greet()
    while True:
        user_input = input("\n🧑 You: ").lower()

        if "time" in user_input:
            print(f"🕒 Current time is: {get_time()}")

        elif "date" in user_input:
            print(f"📅 Today's date is: {get_date()}")

        elif "joke" in user_input:
            print("😂", get_joke())

        elif "who is" in user_input or "what is" in user_input:
            topic = user_input.replace("who is", "").replace("what is", "").strip()
            print("📚", get_info(topic))

        elif "bye" in user_input or "exit" in user_input:
            print("👋 Bye Boss, take care!")
            break

        else:
            print("🤖 I'm still learning, Boss. Try asking something else.")

if __name__ == "__main__":
    mainmenu()
