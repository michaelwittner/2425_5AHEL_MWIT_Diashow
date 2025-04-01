# Vosk installieren: pip install vosk
import wave
import sys
from vosk import Model, KaldiRecognizer

# Pfad zur WAV-Datei (manuell anpassen)
wav_file_path = "testaudio_16000_test01_20s.wav"  # WAV-Endung hinzugefügt

# Pfad zum Vosk-Modell (manuell anpassen)
model_path = "model"

# Überprüfen, ob das Modell existiert
try:
    model = Model(model_path)
except Exception as e:
    print(f"Fehler beim Laden des Modells: {e}")
    sys.exit(1)

# Öffnen der WAV-Datei
try:
    wf = wave.open(wav_file_path, "rb")
except Exception as e:
    print(f"Fehler beim Öffnen der WAV-Datei: {e}")
    sys.exit(1)

# Überprüfen, ob die WAV-Datei die richtigen Parameter hat
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Die WAV-Datei muss Mono, 16 Bit und nicht komprimiert sein.")
    wf.close()
    sys.exit(1)

# Rekognizer initialisieren
recognizer = KaldiRecognizer(model, wf.getframerate())

# Sprachumwandlung
print("Ergebnisse der Spracherkennung:")
while True:
    data = wf.readframes(4000)  # Lese 4000 Frames pro Durchgang
    if len(data) == 0:  # Ende der Datei erreicht
        break
    if recognizer.AcceptWaveform(data):  # Verarbeite Daten
        print(recognizer.Result())  # Zeige das vollständige Ergebnis
    else:
        print(recognizer.PartialResult())  # Optional: Zeige Zwischenergebnisse

# Gib das finale Ergebnis aus
print(recognizer.FinalResult())

# Schließe die WAV-Datei
wf.close()
