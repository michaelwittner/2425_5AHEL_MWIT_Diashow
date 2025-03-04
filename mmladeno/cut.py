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
