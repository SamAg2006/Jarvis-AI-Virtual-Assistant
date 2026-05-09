import speech_recognition as sr
from voice import speak
from commands import processcommand


recognizer = sr.Recognizer()      
if(__name__ == "__main__"): 
    speak("Initializing Jarvis .....")
    r = sr.Recognizer()
    while True:
        
        try:
            # Use the microphone as the audio source
            with sr.Microphone() as source:
                print("Please wait.")
                r.adjust_for_ambient_noise(source, duration=1) # Helps improve accuracy
                print("Listening... Say something!")
                # Capture the audio
                audio = r.listen(source)

            # Recognize speech using Google's free web API
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            if "jarvis" in word.lower():
                speak("Yes Boss ")
                print("Now listening for command...")
                
                with sr.Microphone() as source:
                  print("Jarvis Active.....")
                  r.adjust_for_ambient_noise(source, duration=1) # Helps improve accuracy
                  # Capture the audio
                  audio = r.listen(source)
                  command = r.recognize_google(audio) 
                  processcommand(command)

            
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. {e}")
            