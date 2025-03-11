import cv2
from PIL import Image
import os

"""
VideoGenerator Klasse
description: Diese Klasse erstellt aus mehreren Bildern ein Video.
usage: Erstelle ein TUPLE. In dieser Tuple wird pro Bild, das in ein Video
hinzugefügt werden muss, eine Liste erstellt. Der 0. Index des Bildes ist der
Dateienname und der 1. Index bestimmt, wie lang das Bild im Video erscheint, bevor
das nächste Bild kommt. 

Danach wird ein VideoGenerator Objekt erzeugt. (vg = VideoGenerator())
Mit dem Objekt rufen wir die generate_video_from_images Methode auf. 
Unten steht die Beschreibung dieser Methode und was man angeben kann/muss. 
"""

# TODO: Objektverzeichnis (optional), ansonsten .\ (aktuelles Verzeichnis)
class VideoGenerator:
    # Konstruktor der VideoGenerator Klasse
    def __init__(self):
        print("Video Generator")

    def generate_video_from_images(self, images: tuple, filename: str, fps: int = 30, height: int = None,
                                   width: int = None, codec: str = "mp4v", directory: str = ".") -> None:
        """
        Erstellt ein Video aus einer Liste von Bildern.

        :param images: Liste von Bildpfaden
        :param filename: Name der Ausgabedatei (mp4-Format empfohlen!)
        :param fps: Frames per Second (Standard: 30) (Optional)
        :param width: Breite des Videos (Standard: None) (Optional)
        :param height: Länge des Videos (Standard: None) (Optional)
        :param codec: Codec für das Erstellen des Videos (Standard: mp4v für MP4) (Optional)
        """
        print("Generating video...")

        # Überprüfe, ob die Liste leer ist.
        if not images:
            print("Fehler: Keine Bilder in der Liste!")
            return

        # Laden des ersten Bildes, um die Videogröße zu bestimmen
        first_image = Image.open(os.path.join(directory, images[0][0]))

        # Überprüfe, ob height und width Parameter angegeben wurden
        if height is None and width is None:
            widthVideo, heightVideo = first_image.size
        else:
            widthVideo = width
            heightVideo = height

        # OpenCV VideoWriter initialisieren
        # Audiocodec definieren
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec für MP4-Format
        # Initialisiere Video(-Writer)
        video = cv2.VideoWriter(filename, fourcc, fps, (widthVideo, heightVideo))

        # for Schleife über die Bilder
        for img_path, duration in images:
            # Lade das Bild
            img = cv2.imread(os.path.join(directory, img_path))
            # Überprüfe, ob Bild vorhanden ist
            if img is None:
                print(f"Warnung: Bild {img_path} konnte nicht geladen werden und wird übersprungen.")
                continue

            # Falls notwendig, Bildgröße anpassen
            img = cv2.resize(img, (widthVideo, heightVideo))

            # Anzahl der Frames für das Bild berechnen
            frame_count = int(duration * fps)
            # For Schleife über Frameanzahl
            for _ in range(frame_count):
                # Bild in das Video reinschreiben
                video.write(img)

        # Schließe Videodatei
        video.release()
        print(f"Video erfolgreich erstellt: {filename}")

# Main Programm
def __main__():
    # Definiere Bild Tuple mit Bilddauer (in Sekunden)
    image_list = (["bild1.jpg", 1], ["bild2.jpg", 2], ["bild3.jpg", 1], ["bild4.jpg", 1], ["bild5.jpg", 3], ["bild6.jpg", 1], ["bild7.jpg", 0.5], ["bild8.jpg", 1], ["bild9.jpg", 1], ["bild10.jpg", 1])  # Hier gibt man die Pfade der Bilder an, die zum Video konvertiert werden sollen
    # Generiere Video aus dem Tuple
    vg = VideoGenerator()
    vg.generate_video_from_images(image_list, "output.mp4", directory=".\\proj")

if __name__ == "__main__":
    __main__()
