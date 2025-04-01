import cv2
import numpy as np
import os

# **** slide_transition ****
# image1_path ... Anfangsbild - muss gleich groß wie Endbild sein
# image2_path ... Endbild - muss gleich groß wie Anfangsbild sein
# output_folder ... Ordner in dem die Einzelbiler gespeichert werden - Standardmäßig auf in .\temp
# duration ... Dauer des Übergangs in Sekunden - Standardmäßig auf 1.5s
# fps ... Anzahl an berechneter Frames pro Sekunde - Standardmäßig auf 60
# direction ... Richtung von der das Endbild geschoben wird
# Mögliche Richtungen sind:
# - "SHIFT_LEFT" - Standardeinstellung
# - "SHIFT_RIGHT"
# - "SHIFT_UP"
# - "SHIFT_DOWN"
def slide_transition(image1_path, image2_path, output_folder, duration=1.5, fps=60, direction="SHIFT_LEFT"):
    # Bilder laden
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Prüfen ob gültige Bildpfade angegeben wurden
    if img1 is None or img2 is None:
        print("Fehler: Ein Bild konnte nicht geladen werden.")
        return

    # Gemeinsame Größe festlegen (zur Sicherheit - sollten schon gleich sein)
    height1, width1, _ = img1.shape
    width = width1
    height = height1
    img2 = cv2.resize(img2, (width, height))

    # Anzahl der Frames berechnen
    num_frames = int(duration * fps)
    frame_list = []  # Liste zum Speichern der Dateipfade und Anzeigedauer

    # Speicherpfad erstellen falls es diesen noch nicht gibt
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Überprüfen ob gültige Richtung eingegeben wurde
    if direction not in ["SHIFT_LEFT", "SHIFT_RIGHT", "SHIFT_UP", "SHIFT_DOWN"]:
        print("Fehler: Ungültige Richtung. Verwenden Sie 'SHIFT_LEFT', 'SHIFT_RIGHT', 'SHIFT_UP' oder 'SHIFT_DOWN'.")
        return

    for i in range(num_frames + 1):
        alpha = i / num_frames  # Fortschritt von 0 bis 1
        offset_x = int(alpha * width)  # Pixelverschiebung für horizontale Bewegung
        offset_y = int(alpha * height)  # Pixelverschiebung für vertikale Bewegung

        # Neue leere Leinwand in der gleichen Größe wie die Bilder erstellen
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Bildbereiche für die Bewegung bestimmen
        if direction == "SHIFT_LEFT":
            if offset_x < width:
                frame[:, :width - offset_x] = img1[:, offset_x:]
            if offset_x > 0:
                frame[:, width - offset_x:] = img2[:, :offset_x]
        elif direction == "SHIFT_RIGHT":
            if offset_x < width:
                frame[:, offset_x:] = img1[:, :width - offset_x]
            if offset_x > 0:
                frame[:, :offset_x] = img2[:, width - offset_x:]
        elif direction == "SHIFT_UP":
            if offset_y < height:
                frame[:height - offset_y, :] = img1[offset_y:, :]
            if offset_y > 0:
                frame[height - offset_y:, :] = img2[:offset_y, :]
        elif direction == "SHIFT_DOWN":
            if offset_y < height:
                frame[offset_y:, :] = img1[:height - offset_y, :]
            if offset_y > 0:
                frame[:offset_y, :] = img2[height - offset_y:, :]

        # Bild speichern
        frame_path = os.path.join(output_folder, f"frame_{i:03d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_list.append(f"{frame_path}, {1}/{fps}")

    return frame_list

# Testen der Funktion
# frame_data = slide_transition("bild1.jpg", "bild2.jpg", ".\\temp")
# print("\n".join(frame_data))
