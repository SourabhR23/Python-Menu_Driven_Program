# importing required libraries
# 'pyttsx3' is a text-to-speech conversion library
import pyttsx3
# 'os' is system in-build library
import os

voice = pyttsx3.init()
Voices = voice.getProperty('voices')
# Setting up the voice speed rate
voice.setProperty('rate', 125)   
# Setting up the volume of the voice
voice.setProperty('volume', 0.8)
# Female voice
# If you want to change voice to female, please remove the '#' from below command
#voice.setProperty('voice', Voices[1].id)

# Introduction
x = "Welcome to the menu driven program!\
    From given list below, please select the application which you want to open."
voice.say(x)
voice.runAndWait()

# List of applications
a = ['Google Chrome', 'Paint', 'Windows Media Player', 'Notepad']
n = 0
for apps in a:
    voice.say(a[n])
    print(a[n])
    n += 1
    voice.runAndWait()
    
while True:
    # Taking input from the user
    p = input("\nPlease enter the input: ")
    # For 'Chrome' application
    if ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("chrome" in p.lower()):
        pyttsx3.speak("Opening Chrome.")
        os.system("Chrome")
        
    # For 'Paint' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("paint" in p.lower()):
        pyttsx3.speak("Opening Paint.")
        os.system("mspaint")
        
    # For 'Windows media player' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("windows media player" in p.lower() 
           or "wmplayer" in p.lower() or "media player" in p.lower()):
        pyttsx3.speak("Opening windows media player.")
        os.system("Wmplayer")
        
    # For 'Notepad' application
    elif ('run' in p.lower() or 'open' in p.lower() or 'execute' in p.lower()) and ("notepad" in p.lower()):
        pyttsx3.speak("Opening Notepad.")
        os.system("notepad")
        
    # Exit/Quitting of application codition
    elif ('exit' in p.lower() or 'close' in p.lower() or 'quit' in p.lower()):
        pyttsx3.speak("Thank you for using the application!")
        break
        
    else:
        pyttsx3.speak("Please enter the valid input!")
        print("Please enter the valid input!")


# Sample inputs
# please open Chrome
# I want to draw something so run PAINT application
# Let's dance, execute media player
# Close the program