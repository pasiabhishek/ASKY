import pyttsx3
from datetime import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 190)
engine.setProperty("volume", 1.0)


def talk(query):
    engine.say(query)
    print(f"  ASKY : {query}")
    engine.runAndWait()


def greet():
    current_hour = datetime.now().hour

    if 6 <= current_hour < 12:
        greet_word = "Good Morning"

    elif 12 <= current_hour < 16:
        greet_word = "Good Afternoon"

    elif 16 <= current_hour < 23:
        greet_word = "Good Evening"

    else:
        greet_word = "Good Night"

    talk(f"{greet_word},\n\t i am Asky (Artificial Solutions & Knowledge Yield )... \n\t How can i assist You...")

def open_web(url):
   # webbrowser.open(f"https://www.youtube.com/search?q=master aazam")
    webbrowser.open(url)


def main(cond):
    close= ["bye","see you","close","shutdown","done"]
    while cond:
        user = input("  User : ")
        if "search" in user and "youtube" in user :
            user = user.replace("search", "")
            user = user.replace("youtube", "")
            user = user.replace("on", "")
            user = user.replace("open", "")
            open_web(f"https://www.youtube.com/search?q={user}")
        
        elif "open" in user and "youtube" in user :
            open_web("youtube.com")

            
        elif "open" in user and "google" in user :
            open_web("youtube.com")

        elif "search" in user and "google" in user :
            user = user.replace("search google", "")
            open_web(f"https://www.google.com/search?q={user}")
            main(True)

        elif "what is" in user and "time" in user :
            talk(f"time is {datetime.now().time()}")
        
        
        elif user in close:
             talk(f"OK! {user}")
             return restart()

def restart():
    key = input("   Enter 'restart' to chat again...")

    
    if "start" in key:
        main(True)

            


if __name__ == "__main__":
    greet()
    main(True)
