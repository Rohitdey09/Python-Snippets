#Text to speech with python
import pyttsx3
engine=pyttsx3.init()
text=input("Enter the text you want to convert to speech")
engine.say(text) # 'xxxx' is the text you want to say
engine.runAndWait()
