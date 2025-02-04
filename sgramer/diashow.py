import cv2
import numpy as np
import time


def slide_transition(image1_path, image2_path, duration=1.5, fps=60, max_width=1280, max_height=720):
    # Bilder laden
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        print("Fehler: Konnte ein Bild nicht laden.")
        return

    # Bildgröße anpassen, falls zu groß
    def resize_to_fit(img, max_w, max_h):
        h, w = img.shape[:2]
        scale = min(max_w / w, max_h / h)
        new_size = (int(w * scale), int(h * scale))
        return cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

    img1 = resize_to_fit(img1, max_width, max_height)
    img2 = resize_to_fit(img2, max_width, max_height)

    # Neue Bildgröße ermitteln
    height, width, _ = img1.shape

    # img2 auf die gleiche Größe wie img1 skalieren
    img2 = cv2.resize(img2, (width, height))

    # Anzahl der Frames berechnen
    num_frames = int(duration * fps)

    for i in range(num_frames + 1):
        alpha = i / num_frames  # Fortschritt von 0 bis 1
        offset = int(alpha * width)  # Pixelverschiebung

        # Neue leere Leinwand erstellen
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Bereiche von img1 und img2 bestimmen
        if offset < width:
            frame[:, :width - offset] = img1[:, offset:]
        if offset > 0:
            frame[:, width - offset:] = img2[:, :offset]

        # Bild anzeigen
        cv2.imshow('Diashow Übergang', frame)

        if cv2.waitKey(18) & 0xFF == ord('q'):
            break

    # Endbild anzeigen
    cv2.imshow('Diashow Übergang', img2)
    time.sleep(0.5)  # Kurze Pause

    # Fenster schließen
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Funktion aufrufen
slide_transition("bild1.jpg", "bild2.jpg")

