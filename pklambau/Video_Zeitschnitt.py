import cv2

# Eingabe für den Namen der Videodatei, Start- und Endzeitpunkt
video_name = input("Gib den Namen der Videodatei ein (z.B. drift.mp4): ")
start_time = float(input("Gib den Startzeitpunkt in Sekunden ein (z.B. 2.0): "))
end_time = float(input("Gib den Endzeitpunkt in Sekunden ein (z.B. 10.0): "))

# Video öffnen
cap = cv2.VideoCapture(video_name)

if not cap.isOpened():
    print("Fehler: Video konnte nicht geöffnet werden")
    exit()

# Video-Parameter
fps = cap.get(cv2.CAP_PROP_FPS)  # Bildrate des Videos
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# VideoWriter für das Ausgabevideo erstellen
output_name = "output_cut.mp4"
# Der FourCC-Code (Four Character Code) für den MP4-Codec (mp4v) wird mit der Funktion VideoWriter_fourcc() erstellt.
# Diese Funktion erwartet vier separate Zeichen, weshalb der Stern (*) vor 'mp4v' verwendet wird,
# um den String 'mp4v' in einzelne Zeichen zu entpacken und an die Funktion zu übergeben.
# Der resultierende FourCC-Code wird in der Variablen 'fourcc' gespeichert.
# Dieser Code wird später verwendet, um das Video im MP4-Format zu speichern.
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_name, fourcc, fps, (frame_width, frame_height))

# Frames zum Startzeitpunkt springen
start_frame = int(start_time * fps)
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# Das Video von start_time bis end_time schneiden
while cap.isOpened():
    current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) / fps

    if current_frame >= end_time:
        break  # Video beenden, wenn der Endzeitpunkt erreicht ist

    # Liest das nächste Frame aus dem Video.
    # 'cap.read()' gibt zwei Werte zurück:
    # 1. 'ret' (Boolean): Gibt an, ob das Lesen erfolgreich war (True) oder das Ende des Videos erreicht wurde (False).
    # 2. 'frame' (Array): Enthält das aktuelle Videobild als NumPy-Array (RGB-Farbwerte für jedes Pixel).
    # Falls das Video zu Ende ist oder ein Fehler auftritt, wird 'ret' False sein, und 'frame' ist ungültig.
    ret, frame = cap.read()

    if not ret:
        break

    # Das aktuelle Frame in das Ausgabefile schreiben
    out.write(frame)

    # Optional: Das aktuelle Frame anzeigen
    cv2.imshow("Video", frame)

# Freigabe der Videoressourcen und Fenster schließen
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Das Video wurde erfolgreich geschnitten und als {output_name} gespeichert.")
