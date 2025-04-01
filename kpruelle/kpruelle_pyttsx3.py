import pyttsx3
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
for voice in voices:
    print(f"ID: {voice.id}\nName: {voice.name}\n")

# engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

# Deutsche Stimme auswählen (nimm die ID der gewünschten deutschen Stimme)
german_voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_DE-DE_HEDDA_11.0'
engine.setProperty('voice', german_voice_id)

engine.say("Hallo Welt, das ist ein Test!")
engine.runAndWait()

#engine.say("Hello World!")
#engine.say('My current speaking rate is ' + str(rate))
#engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
