import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # changing voice to female voice
engine.setProperty('rate', 200) # changing the rate of the assistant's voice
engine.say("Hello, I'm your computer. How can I help you?")


engine.runAndWait()