import cv2
import numpy as np
import os

def slide_transition(image1_path, image2_path, output_folder, duration=1.5, fps=40, direction="SHIFT_LEFT"):
    # Bilder laden
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        print("Fehler: Konnte ein Bild nicht laden.")
        return

    # Bildgrößen ermitteln
    height1, width1, _ = img1.shape
    height2, width2, _ = img2.shape

    
    # Gemeinsame Größe festlegen (z. B. anhand des ersten Bildes)
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
    if direction not in ["SHIFT_LEFT", "SHIFT_RIGHT"]:
        print("Fehler: Ungültige Richtung. Verwenden Sie 'SHIFT_LEFT' oder 'SHIFT_RIGHT'.")
        return

    for i in range(num_frames + 1):
        alpha = i / num_frames  # Fortschritt von 0 bis 1
        offset = int(alpha * width)  # Pixelverschiebung für den Übergang

        # Neue leere Leinwand in der gleichen Größe wie die Bilder erstellen
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Bildbereiche für die Bewegung bestimmen
        if direction == "SHIFT_LEFT":
            if offset < width:
                frame[:, :width - offset] = img1[:, offset:]
            if offset > 0:
                frame[:, width - offset:] = img2[:, :offset]
        elif direction == "SHIFT_RIGHT":
            if offset < width:
                frame[:, offset:] = img1[:, :width - offset]
            if offset > 0:
                frame[:, :offset] = img2[:, width - offset:]

        # Bild speichern
        frame_path = os.path.join(output_folder, f"frame_{i:03d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_list.append(f"{frame_path}, {1}/{fps}")

    return frame_list

# Funktion aufrufen
frame_data = slide_transition("bild1.jpg", "bild2.jpg", ".\\Bilder", 1.5, 30, "SHIFT_RIGHT")

print("\n".join(frame_data))
