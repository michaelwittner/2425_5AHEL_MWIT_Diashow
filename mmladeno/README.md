# Cut - mmladeno
## 04.02.2025
* Öffnen einer MP3-Datei mit pydub.
* Audio startet bei 0 kann man aber auch selber definieren start_wert:end_wert


## 25.02.2025
* Packages haben nicht funktioniert
* pydub und die dazugehörigen Packages heruntergeladen (audioop, ffmpeg und pydub)

https://github.com/BtbN/FFmpeg-Builds/releases
* Extrahiert in: H:\MWIT\ffmpeg\bin 
* Pfad um H:\MWIT\ffmpeg\bin ergänzen

## 04.03.2025
* Ersten 10 Sekunden einer Audio-Datei abspielen (first_10_seconds.mp3):
```
from pydub import AudioSegment
import audioop

# Öffnen einer MP3-Datei mit pydub.
song = AudioSegment.from_mp3("WhoYouFoolin.mp3")

# pydub arbeitet in millisekunden
ten_seconds = 10 * 1000

# Startet bei 0 kann man aber auch selber definieren start_wert:end_wert
first_10_seconds = song[:ten_seconds]

# save file
first_10_seconds.export("first_10_seconds.mp3", format="mp3")
print("New Audio file is created and saved")
```

* Beginnend bei der 10. Sekunde und endend bei der 30. Sekunde (cut_audio.mp3):

```
from pydub import AudioSegment

# Öffnen einer MP3-Datei mit pydub.
song = AudioSegment.from_mp3("WhoYouFoolin.mp3")

# pydub arbeitet in millisekunden
start_wert = 10 * 1000
end_wert = 30 * 1000

# Startet bei 0 kann man aber auch selber definieren start_wert:end_wert
cut_audio = song[start_wert:end_wert]

# save file
cut_audio.export("cut_audio.mp3", format="mp3")
print("New Audio file is created and saved")
```

* Cut-Left:
```
from pydub import AudioSegment


def cut_audio(file_name, result_length, cut_direction):
    # Öffnen der MP3-Datei
    song = AudioSegment.from_mp3(file_name)

    # Umrechnung der gewünschten Länge in Millisekunden
    result_length_ms = result_length * 1000

    # Prüfen der Cut-Richtung
    if cut_direction == "CUT-LEFT":
        # Vom Anfang wegschneiden: Die letzten 'result_length' Sekunden behalten
        result_audio = song[-result_length_ms:]
    elif cut_direction == "CUT-RIGHT":
        # Vom Ende wegschneiden: Die ersten 'result_length' Sekunden behalten
        result_audio = song[:result_length_ms]
    else:
        raise ValueError("Bitte 'CUT-LEFT' oder 'CUT-RIGHT' angeben.")

    # Speichern der neuen Datei
    result_audio.export(f"cut_{cut_direction}_{result_length}_seconds.mp3", format="mp3")
    print(f"Neue Datei '{f'cut_{cut_direction}_{result_length}_seconds.mp3'}' wurde erstellt und gespeichert.")


# Beispielaufruf der Funktion
cut_audio("WhoYouFoolin.mp3", 20,"CUT-LEFT")  # Beispiel für CUT-LEFT (erste 5 Sekunden entfernen, um 20 Sekunden zu erhalten)
```