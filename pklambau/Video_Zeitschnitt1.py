import cv2

def cut(video_name, start_time, stop_time):
    # Öffnet das Video zur Bearbeitung
    cap = cv2.VideoCapture(video_name)

    # Prüft, ob das Video erfolgreich geöffnet wurde
    if not cap.isOpened():
        print("Fehler: Video konnte nicht geöffnet werden")
        return

    # Ermittelt die Bildrate (FPS) des Videos
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Ermittelt die Breite und Höhe der Frames
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Erstellt einen VideoWriter für die Ausgabe (geschnittenes Video)
    output_name = "output_cut.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_name, fourcc, fps, (frame_width, frame_height))

    # Berechnet den Start-Frame basierend auf der Startzeit und FPS
    start_frame = int(start_time * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Schleife zum Ausschneiden des Videos
    while cap.isOpened():
        # Bestimmt das aktuelle Zeit-Stempel (in Sekunden)
        current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) / fps

        # Beendet die Verarbeitung, wenn die Stop-Zeit erreicht wurde
        if current_frame >= stop_time:
            break

        # Liest den aktuellen Frame
        ret, frame = cap.read()
        if not ret:
            break

        # Schreibt den Frame in die Ausgabedatei
        out.write(frame)

    print(f"Das Video wurde erfolgreich geschnitten und als {output_name} gespeichert.")

    # Freigeben der Ressourcen
    cap.release()
    out.release()


def generateThumbnail(video_name, thumbnail_frame_number):
    # Öffnet das Video
    cap = cv2.VideoCapture(video_name)

    # Prüft, ob das Video erfolgreich geöffnet wurde
    if not cap.isOpened():
        print("Fehler: Video konnte nicht geöffnet werden")
        return

    # Ermittelt die Breite und Höhe der Frames
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    thumbnail_frame = None

    # Durchsucht das Video bis zum gewünschten Thumbnail-Frame
    while cap.isOpened():
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        # Prüft, ob der gewünschte Frame erreicht wurde
        if current_frame == thumbnail_frame_number:
            ret, frame = cap.read()
            if ret:
                thumbnail_frame = frame
            break

        ret, frame = cap.read()
        if not ret:
            break

    # Lädt das Overlay-Bild mit Alphakanal (z.B. PNG mit Transparenz)
    overlay_image = cv2.imread("overlay1.jpg", cv2.IMREAD_UNCHANGED)

    # Prüft, ob sowohl das Thumbnail als auch das Overlay geladen wurden
    if thumbnail_frame is not None and overlay_image is not None:
        if overlay_image.shape[2] == 4:  # Prüft, ob das Overlay einen Alphakanal hat
            # Skaliert das Overlay auf eine feste Größe (falls notwendig)
            overlay_resized = cv2.resize(overlay_image, (250, 250))

            # Berechnet die Position des Overlays (zentriert im Frame)
            x_offset = (frame_width - overlay_resized.shape[1]) // 2
            y_offset = (frame_height - overlay_resized.shape[0]) // 2

            # Extrahiert den Alphakanal (Transparenz) des Overlays
            alpha_channel = overlay_resized[:, :, 3] / 255.0
            alpha_inv = 1.0 - alpha_channel

            # Überlagert das Overlay auf das Thumbnail unter Berücksichtigung der Transparenz
            for c in range(3):  # Für die Farbkanäle R, G, B
                thumbnail_frame[y_offset:y_offset + overlay_resized.shape[0],
                x_offset:x_offset + overlay_resized.shape[1], c] = (
                        alpha_channel * overlay_resized[:, :, c] +
                        alpha_inv * thumbnail_frame[y_offset:y_offset + overlay_resized.shape[0],
                                    x_offset:x_offset + overlay_resized.shape[1], c]
                )

            # Speichert die generierte Miniaturansicht
            cv2.imwrite("Miniaturansicht.png", thumbnail_frame)
            print("Miniaturansicht gespeichert als Miniaturansicht.png")
        else:
            print("Fehler: Overlay-Bild hat keinen Alphakanal")

    # Freigeben der Ressourcen
    cap.release()


def getLastFrame(video_name):
    # Öffnet das Video
    cap = cv2.VideoCapture(video_name)

    # Prüft, ob das Video erfolgreich geöffnet wurde
    if not cap.isOpened():
        print("Fehler: Video konnte nicht geöffnet werden")
        return None

    # Springt direkt zum letzten Frame des Videos
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)

    # Liest den letzten Frame aus
    ret, frame = cap.read()
    cap.release()

    # Prüft, ob der Frame erfolgreich gelesen wurde
    if ret:
        # Speichert den letzten Frame als Bild
        cv2.imwrite("LastFrame.png", frame)
        print("Letzter Frame gespeichert als LastFrame.png")
        return frame
    else:
        print("Fehler: Letzter Frame konnte nicht gelesen werden")
        return None


# Eingabe für den Namen der Videodatei, Start- und Endzeitpunkt
video_name = input("Gib den Namen der Videodatei ein (z.B. drift.mp4): ")
start_time = float(input("Gib den Startzeitpunkt in Sekunden ein (z.B. 2.0): "))
end_time = float(input("Gib den Endzeitpunkt in Sekunden ein (z.B. 10.0): "))
thumbnail_frame_number = int(input("Gib die Frame-Nummer für die Miniaturansicht ein (z.B. 10): "))


# Aufruf der Funktionen
cut(video_name, start_time, end_time)
generateThumbnail(video_name, thumbnail_frame_number)
getLastFrame(video_name)