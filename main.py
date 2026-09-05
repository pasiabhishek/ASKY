import warnings
import pyttsx3
import webbrowser
import wikipedia
from datetime import datetime
from urllib.parse import quote
import speech_recognition as sr

# Just hiding the warning from the wikipedia package
warnings.filterwarnings("ignore")

# ASKY stands for Artificial Solutions for Knowledge Yield
ASSISTANT_NAME = "ASKY"

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        query = ""
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}") 
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, I could not request results from Google Speech Recognition service.")
    return query

def talk(message):
    # Start the voice engine whenever ASKY needs to speak
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    print(f"  {ASSISTANT_NAME} : {message}")

    engine.say(message)
    engine.runAndWait()
    engine.stop()


def greet():
    # Change the greeting depending on the current time
    hour = datetime.now().hour

    if 6 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 16:
        greeting = "Good Afternoon"
    elif 16 <= hour < 23:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    talk(
        f"{greeting}.\n\t\t "
        f"I am Artificial Solutions for Knowledge Yield, also known as asky. \n\t\t "
        "How can I assist you?"
    )


def open_website(url):
    # Open the given link in the default browser
    webbrowser.open(url)


def search_youtube(query):
    # Search the user's query directly on YouTube
    talk(f"Searching YouTube for {query}.")

    query = quote(query)

    open_website(
        f"https://www.youtube.com/results?search_query={query}"
    )


def search_google(query):
    # Search Google for whatever the user asks
    talk(f"Searching Google for {query}.")

    query = quote(query)

    open_website(
        f"https://www.google.com/search?q={query}"
    )



def search_wikipedia(topic):
    # Get a short answer from Wikipedia
    try:
        result = wikipedia.summary(topic, sentences=2)
        talk(result)

    except wikipedia.exceptions.DisambiguationError:
        # This happens when Wikipedia finds more than one matching topic
        talk("There are multiple results. Please be more specific.")

    except wikipedia.exceptions.PageError:
        # The topic doesn't exist on Wikipedia
        talk("Sorry, I could not find that topic.")

    except Exception as e:
        # Catch any unexpected error so ASKY doesn't crash
        print(e)
        talk("Something went wrong while searching Wikipedia.")


def main():

    # These words will close the assistant
    exit_commands = [
        "bye",
        "exit",
        "close",
        "shutdown",
        "done"
    ]

    while True:

        # user = input("  You : ").lower().strip()
        user = input("  You : ").lower().strip()

        # Close ASKY
        if user in exit_commands:

            talk("Okay, shutting down ASKY.")
            break

        # Open YouTube
        elif user.startswith("open youtube"):

            talk("Opening YouTube.")
            open_website("https://www.youtube.com")

        # Search something on YouTube
        elif "search" in user and "youtube" in user:

            query = user.replace("search", "")
            query = query.replace("youtube", "")
            query = query.replace("on", "")
            query = query.strip()

            if query:
                search_youtube(query)
            else:
                talk("What should I search on YouTube?")

        # Open Google
        elif user.startswith("open google"):

            talk("Opening Google.")
            open_website("https://www.google.com")

        # Search something on Google
        elif "search" in user and "google" in user:

            query = user.replace("search", "")
            query = query.replace("google", "")
            query = query.replace("on", "")
            query = query.strip()

            if query:
                search_google(query)
            else:
                talk("What should I search on Google?")

        # Search Wikipedia
        elif "wikipedia" in user:

            topic = user.replace("wikipedia", "")
            topic = topic.replace("search", "")
            topic = topic.strip()

            if topic:
                search_wikipedia(topic)
            else:
                talk("What should I search on Wikipedia?")

        # Tell the current time
        elif "time" in user:

            current_time = datetime.now().strftime("%I:%M %p")

            talk(f"The current time is {current_time}.")

        # ASKY doesn't know this command yet
        else:

            talk("I don't know how to perform that task yet.")


# Start ASKY when this file is run
if __name__ == "__main__":

    greet()
    main()


