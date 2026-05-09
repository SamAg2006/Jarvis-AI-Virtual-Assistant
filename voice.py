# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)    
#     engine.say(text)
#     engine.runAndWait()
#     time.sleep(1)


from gtts import gTTS
import pygame
import time
import os
# This is the speaking engine that gives output to user by simply speaking 

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")  # replace with your file path

    # Play the music
    pygame.mixer.music.play()

    print("Playing audio...")

    # Keep the program running while music is playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    
    pygame.mixer.music.unload() 
    os.remove("temp.mp3")