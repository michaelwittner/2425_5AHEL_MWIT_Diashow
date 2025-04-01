- 04.02.2025:

    Ausprobieren der Modelle gTTS und pyttsx3 -> beide funktionieren nur online

    https://www.geeksforgeeks.org/convert-text-speech-python/


- 25.02.2025:
 
    Fehlerbehebungen in Pycharm

    Offline-Versuch von pyttsx3: https://github.com/nateshmbhat/pyttsx3/tree/master

    -> Package sehr klein (nur einige 100kB) -> funktioniert offline nicht


- 04.03.2025:
 
    Tests und Recherche zu pyttsx3 

    --> hängt vermutlich mit dem Windwos Sprachmodell zusammen, Installation hat allerdings nicht funktioniert

    
- 11.03.2025:
 
    Testen von pyttsx3 auf Notepad (offline) --> hat funktioniert

    Tesen der deutschen Sprache auf Notepad --> hat ebenfalls funktioniert

    --> Es funktioniert jede Sprache, dessen Sprachpaket auf einem Rechner installiert ist
    
    TODO: Sprache schön auswählen können ('Deutsch', nicht Sprachpaketname)

    TODO: Speech zu Text --> Wav-File --> Untertitel


- 18.03.2025:
 
    Speech to Text: vosk, (pyaudio)

    Man muss folgendes Model herunterladen: https://alphacephei.com/vosk/models


- 01.04.2025:
 
    Testen der Speech to Text Funktion mittels Online-Testfiles und eigener Aufnahmen

    --> Bei eigenen Audiodateien (m4a-Dateiendung) müssen diese mittels Online-Converter (https://convertio.co/de/m4a-wav/) zu einer wav-Datei umgewandelt werden
