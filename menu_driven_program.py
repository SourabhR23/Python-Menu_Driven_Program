# importing required libraries
# 'pyttsx3' is a text-to-speech conversion library
import pyttsx3
# 'os' is python in-build library
import os

voice = pyttsx3.init()
Voices = voice.getProperty('voices')
# Setting up the voice speed rate
voice.setProperty('rate', 170)   
# Setting up the volume of the voice
voice.setProperty('volume', 0.8)
# For having Female voice
#voice.setProperty('voice', Voices[1].id)

# Introduction
x = "Welcome to the menu driven program!\nI am here to direct you to the application you want to open."
voice.say(x)
print(x)
voice.runAndWait()
pyttsx3.speak("Please enter the application: ")
    
while True:
    # Taking input from the user
    p = input("\nPlease enter the application you want to open: ")
    
    # For 'Chrome' application
    if ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("chrome" in p.lower()):
        pyttsx3.speak("OK. Opening Chrome.")
        os.system("Chrome")
        
    # For 'Paint' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("paint" in p.lower()):
        pyttsx3.speak("OK. Opening Paint.")
        os.system("mspaint")
        
    # For 'Windows media player' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("windows media player" in p.lower() 
           or "wmplayer" in p.lower() or "media player" in p.lower()):
        pyttsx3.speak("OK. Opening windows media player.")
        os.system("Wmplayer")
        
    # For 'Notepad' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("notepad" in p.lower()):
        pyttsx3.speak("OK. Opening Notepad.")
        os.system("notepad")
    
    # For 'Calculator' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("calculator" in p.lower()):
        pyttsx3.speak("OK. Opening Calculator.")
        os.system("calc")
        
    # Exit/Quitting of application codition
    elif ('exit' in p.lower() or 'close' in p.lower() or 'quit' in p.lower()):
        pyttsx3.speak("OK! Thank you for using the application! See you soon!")
        break
        
    else:
        pyttsx3.speak("Please enter the valid input!")
        print("Please enter the valid input!")
