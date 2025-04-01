import cv2
import numpy as np

def cut(video_name, start_time, stop_time):
    # Video öffnen
    cap = cv2.VideoCapture(video_name)

    if not cap.isOpened():
        print("Fehler: Video konnte nicht geöffnet werden")
        return

    # Video-Parameter
    fps = cap.get(cv2.CAP_PROP_FPS)  # Bildrate des Videos
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # VideoWriter für das Ausgabevideo erstellen
    output_name = "output_cut.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_name, fourcc, fps, (frame_width, frame_height))

    # Frames zum Startzeitpunkt springen
    start_frame = int(start_time * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Das Video von start_time bis stop_time schneiden
    while cap.isOpened():
        current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) / fps

        if current_frame >= stop_time:
            break  # Video beenden, wenn der Endzeitpunkt erreicht ist

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

def generateThumbnail(video_name, thumbnail_frame_number, overlay_image_path):
    # Video öffnen
    cap = cv2.VideoCapture(video_name)

    if not cap.isOpened():
        print("Fehler: Video konnte nicht geöffnet werden")
        return

    # Video-Parameter
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    thumbnail_frame = None

    # Das Video bis zum angegebenen Thumbnail-Frame durchsuchen
    while cap.isOpened():
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        if current_frame == thumbnail_frame_number:
            ret, frame = cap.read()
            if ret:
                thumbnail_frame = frame
            break

        ret, frame = cap.read()
        if not ret:
            break

    # Overlay-Bild laden
    overlay_image = cv2.imread(overlay_image_path)

    if thumbnail_frame is not None and overlay_image is not None:
        # Position des Overlays (zentriert)
        x_offset = (frame_width - overlay_image.shape[1]) // 2
        y_offset = (frame_height - overlay_image.shape[0]) // 2

        # Das Overlay-Bild direkt auf das Miniaturbild anwenden
        thumbnail_frame[y_offset:y_offset + overlay_image.shape[0], x_offset:x_offset + overlay_image.shape[1]] = overlay_image

        # Miniaturansicht speichern
        cv2.imwrite("Miniaturansicht.png", thumbnail_frame)
        print("Miniaturansicht gespeichert als Miniaturansicht.png")

    cap.release()



# Eingabe für den Namen der Videodatei, Start- und Endzeitpunkt
video_name = input("Gib den Namen der Videodatei ein (z.B. drift.mp4): ")
start_time = float(input("Gib den Startzeitpunkt in Sekunden ein (z.B. 2.0): "))
end_time = float(input("Gib den Endzeitpunkt in Sekunden ein (z.B. 10.0): "))
thumbnail_frame_number = int(input("Gib die Frame-Nummer für die Miniaturansicht ein (z.B. 10): "))
overlay_image_path = input("Gib den Pfad der Overlay Datei ein (z.B. overlay.jpg): ")


# Aufruf der Funktionen
cut(video_name, start_time, end_time)
generateThumbnail(video_name, thumbnail_frame_number, overlay_image_path)
