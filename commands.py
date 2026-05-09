import webbrowser
from voice import speak
from brain import ask_ai
import requests
import musiclibrary
import json
from dotenv import load_dotenv
import os

load_dotenv()


# This is the news section from where virtual assistant Jarvis tell today's news
newsapi = os.getenv("NEWS_API")

def get_news():
            api_key = f"{newsapi}"
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

            r = requests.get(url)
            data = r.json()

            articles = data.get("articles", [])

            if not articles:
                speak("No news found")
                return

            speak("Here are today's top headlines")

            for i, article in enumerate(articles[:5]):  # Top 5 news
                headline = article["title"]
                print(f"{i+1}. {headline}")
                speak(headline)    



def processcommand(c,speak_output=True):
    
    response = ""
    
    if "open google" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://google.com")
        response = "Opening Google..."
    elif "open youtube" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://www.youtube.com/")
        response = "Opening Youtube..."
    elif "open chatgpt" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://chatgpt.com/")
        response = "Opening Chatgpt..."
    elif "open facebook" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://www.facebook.com/")
        response = "Opening Facebook..."
    elif "open instagram" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://www.instagram.com/")
        response = "Opening Instagram..."
    elif "open whatsapp" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://web.whatsapp.com/")
        response = "Opening Whatsapp..."
    elif "open linkedin" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://www.linkedin.com/feed/")
        response = "Opening Linkedin..."
    elif "open games" in c.lower():
        speak("Offcourse")
        webbrowser.open("https://poki.com/")
        response = "Opening Games section..."

    elif "samyak" in c.lower():
        speak("Samyak Agrawal is the developer of Jarvis which is a virtual AI assistant  ")
        webbrowser.open("https://www.linkedin.com/in/samyak-agrawal-503797321/")
    
    elif c.lower().startswith("play"):
        speak("Offcourse")
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        response = f"Playing {song}"

    elif "news" in c.lower():
        speak("Offcourse")
        get_news()

    else:
        print("You said : " , c)
        print("Thinking... please wait !")
        speak("Thinking...please wait")
        response = ask_ai(c)
        print(response)
        


    # 🔥 handle both GUI + voice
    if speak_output:
        speak(response)

    return response