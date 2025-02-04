import pyttsx3

# Initialisiere den Konverter
engine = pyttsx3.init()

# Öffne und lies die Textdatei
with open('file.txt', 'r') as file:
    text = file.read()

# Konvertiere Text in Sprache
engine.say(text)
engine.runAndWait()