import cv2
import numpy as np
import os

def diagonal_blend(image1_path, image2_path, dst_dir, duration, fps, direction='tl'):
    """
    Erstellt eine Diagonalblenden-Animation zwischen zwei Bildern in einer bestimmten Richtung.
    :param image1_path: Pfad zum ersten Bild
    :param image2_path: Pfad zum zweiten Bild
    :param dst_dir: Verzeichnis zum Speichern der resultierenden Bilder
    :param duration: Dauer der Animation in Sekunden
    :param fps: Anzahl der Bilder pro Sekunde
    :param direction: Richtung der Blende ('tl', 'tr', 'bl', 'br')
    """

    # Bilder laden
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        print("Fehler: Ein oder beide Bilder konnten nicht geladen werden.")
        return

    height, width, _ = img1.shape
    steps = int(duration * fps)

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for i in range(steps + 1):
        mask = np.zeros((height, width), dtype=np.float32)
        diag_position = int((i / steps) * (width + height))

        for y in range(height):
            for x in range(width):
                if direction == 'tl':  # oben links -> unten rechts
                    condition = x + y < diag_position
                elif direction == 'tr':  # oben rechts -> unten links
                    condition = (width - x) + y < diag_position
                elif direction == 'bl':  # unten links -> oben rechts
                    condition = x + (height - y) < diag_position
                elif direction == 'br':  # unten rechts -> oben links
                    condition = (width - x) + (height - y) < diag_position
                else:
                    raise ValueError("Ungültige Richtung. Erlaubt sind: 'tl', 'tr', 'bl', 'br'.")

                if condition:
                    mask[y, x] = 1.0

        blended = (img1 * (1 - mask[:, :, np.newaxis]) + img2 * (mask[:, :, np.newaxis])).astype(np.uint8)

        filename = os.path.join(dst_dir, f"Diagonalblende_{i:03d}.png")
        cv2.imwrite(filename, blended)


#- `"tl"` = oben links → unten rechts (standard)
#- `"tr"` = oben rechts → unten links
#- `"bl"` = unten links → oben rechts
#- `"br"` = unten rechts → oben links
diagonal_blend('bild1.png', 'bild2.png', 'output_images', duration=1, fps=80, direction='br')









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
