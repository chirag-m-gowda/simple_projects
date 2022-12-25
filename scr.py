# BUILDING A VOICE ASSISTANT WITH PYTHON (SPEECH COMMAND RECOGNITION)

# Download and install all the below mentioned packages before implementing the project. 

import speech_recognition as sr # 'sr' is just any variable name. 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()  #initialize engine.
voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[1].id) # change voice of assistant to female



def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command(): #function to take input from user
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey siri' in command:
                command = command.replace('hey siri','')
                print (command)
    except:
        pass
    return command

def run_siri(): #function to recognize certain command and give an appropriate reply
    command= take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command: 
        time = datetime.datetime.now().strftime('%I:%M %p')
        print (time)
        talk('current time is' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about','')
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())   
    else:
        talk('sorry i was unable to hear you clearly, could you please repeat the command')    
      
"""
you can add more functionality and recognize various commands,
just by adding elif blocks in the above function and importing the necessary packages.
"""

while True:  #run assistant continuously
  run_siri()