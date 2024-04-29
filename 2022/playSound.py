import pyttsx3
import sys

text = "".join(sys.argv[1:])

engine = pyttsx3.init()
engine.setProperty('rate', 400)
engine.say(text)
engine.runAndWait()
