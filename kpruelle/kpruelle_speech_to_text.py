import sys
import os
import wave
import json
from vosk import Model, KaldiRecognizer

# Load the Vosk model
model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Open the audio stream
wf = wave.open("/path/to/audio.wav", "rb")

if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

# Process the audio stream
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(result)
    else:
        print(rec.PartialResult())

# Final result
print(rec.FinalResult())
