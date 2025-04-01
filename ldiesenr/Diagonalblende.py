import cv2
import numpy as np
import os


def diagonal_blend(image1_path, image2_path, dst_dir, duration, fps):
    """
    Erstellt eine Diagonalblenden-Animation zwischen zwei Bildern und speichert jedes Frame als Bilddatei.

    :param image1_path: Pfad zum ersten Bild
    :param image2_path: Pfad zum zweiten Bild
    :param dst_dir: Verzeichnis zum Speichern der resultierenden Bilder
    :param duration: Dauer der Animation in Sekunden
    :param fps: Anzahl der Bilder pro Sekunde (Frames per Second)
    """
    # Bilder laden
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Überprüfen, ob beide Bilder erfolgreich geladen wurden
    if img1 is None or img2 is None:
        print("Fehler: Ein oder beide Bilder konnten nicht geladen werden.")
        return

    # Bildgröße bestimmen
    height, width, _ = img1.shape

    # Berechnung der Anzahl der Schritte basierend auf Dauer und FPS
    steps = int(duration * fps)

    # Sicherstellen, dass das Zielverzeichnis existiert
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Generierung der Blendenbilder
    for i in range(steps + 1):
        # Maske für die Diagonalblende erstellen
        mask = np.zeros((height, width), dtype=np.float32)
        diag_position = int((i / steps) * (width + height))  # Position der Blende

        # Maske füllen: Setze Pixel innerhalb der Diagonalblende auf 1
        for y in range(height):
            for x in range(width):
                if x + y < diag_position:
                    mask[y, x] = 1.0

        # Überblenden der beiden Bilder basierend auf der Maske
        blended = (img1 * (1 - mask[:, :, np.newaxis]) + img2 * (mask[:, :, np.newaxis])).astype(np.uint8)

        # Generierten Frame speichern
        filename = os.path.join(dst_dir, f"Diagonalblende_{i:03d}.png")
        cv2.imwrite(filename, blended)

# Beispielaufruf mit Speicherpfad
diagonal_blend('bild1.png', 'bild2.png', 'output_images', duration=1, fps=80)












"""
def resize_images(input_dir, output_dir, size):
    
    Skaliert alle Bilder in einem Verzeichnis auf eine vorgegebene Größe.

    :param input_dir: Pfad zum Eingabeverzeichnis mit Bildern
    :param output_dir: Pfad zum Ausgabeordner für die skalierten Bilder
    :param size: Zielgröße als Tuple (breite, höhe)
    
    # Überprüfen, ob das Ausgabe-Verzeichnis existiert, falls nicht, erstellen
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Durch alle Dateien im Eingangsverzeichnis iterieren
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)  # Vollständiger Pfad zur Eingabedatei
        output_path = os.path.join(output_dir, filename)  # Vollständiger Pfad zur Ausgabe-Datei

        # Überprüfen, ob die Datei ein unterstütztes Bildformat hat
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img = cv2.imread(input_path)  # Bild laden

            if img is not None:
                resized_img = cv2.resize(img, size)  # Bild auf die gewünschte Größe skalieren
                cv2.imwrite(output_path, resized_img)  # Skaliertes Bild speichern
                print(f"Gespeichert: {output_path}")
            else:
                print(f"Fehler beim Laden von {input_path}")  # Fehler beim Laden des Bildes melden


# Beispielaufruf
resize_images('input_images', 'output_images', (800, 600))
"""
