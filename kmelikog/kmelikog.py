import cv2
from PIL import Image
import os
import shutil

"""
VideoGenerator Klasse
description: Diese Klasse erstellt aus mehreren Bildern ein Video.
usage: Legen Sie ein VideoGenerator Objekt an. Erstelle ein TUPLE mithilfe 
der "generate_image_list" Methode. In dieser Tuple wird pro Bild, das in ein Video
hinzugefügt werden muss, eine Liste erstellt. Der 0. Index des Bildes ist der
Dateienname und der 1. Index bestimmt, wie lang das Bild im Video erscheint, bevor
das nächste Bild kommt. 
Danach wird die generate_video_from_images Methode aufgerufen. 
Unten steht die Beschreibung dieser Methode und was man angeben kann/muss. 
Gegebenenfalls kann man die delete_directory aufrufen, um das Verzeichnis, in dem die
Bilder sind, zu löschen.

Andere Methode (benutzerfreundlich, empfohlen!): Rufen Sie die generate_video_from_path Methode auf.
Als Parameter müssen Sie nur den Pfad, worin die Bilder gespeichert sind, angeben, sowie 
die Ausgabedatei. Optional können Sie auch die fps angeben, normalerweise beträgt sie 30.
Nach Aufruf dieser Methode wird aus den Bildern ein Video erstellt und das Verzeichnis, worin
die Bilder gespeichert sind, gelöscht.
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

    def generate_image_list(self, path, fps):
        """
        Diese Methode generiert ein Tuple aus Bildern eines Verzeichnisses
        Diese Methode wird für die "generate_video_from_images" Methode gebraucht,
        da dieser "images" als Parameter braucht

        param: path ... Pfad des Verzeichnisses, wo die Bilder darin gespeichert sind
        param: fps  ... Frames per second (30 empfohlen)
        """
        print("Generating image list...")
        list_files = os.listdir(path) # os.listdir() gibt eine Liste von allen Files in einem Verzeichnis aus
        list_files.sort()
        print(list_files)
        image_paths = [] # Erstelle neue Liste

        # For-Schleife über alle (Bild-)dateien in der list_files Liste
        for img_path in list_files:
            # Füge neues Element in image_paths Liste hinzu,
            # bestehend aus Bildpfad+Bilddateienname und fps (in Sekunden) für die Bilddauer

            # Überprüfe, ob die Datei eine Bilddatei ist (z.B. PNG oder JPG File)
            if img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_paths.append([f"{path}/{img_path}", 1/fps])
            else:
                print("Datei ist keine Bilddatei!")

        image_tuple = tuple(image_paths) # Wandelt die Liste in ein Tuple um
        print(image_tuple)
        return image_tuple

    def delete_directory(self, path):
        """
        Löscht ein Verzeichnis
        Diese Methode wird gebraucht, da die Applikation von Herrn Dürnberger Bilder in einem TEMP Verzeichnis speichert
        Damit das Verzeichnis nicht mit Bildern überfüllt wird, wurde dafür diese Methode erstellt

        param: path ... Pfad des Verzeichnisses
        """
        shutil.rmtree(path)

    def generate_video_from_path(self, path, filename, fps: int=30):
        """
        Erstellt ein Video aus einer Liste von Bildern.
        Dabei gibt man nur den Pfad, worin die Bilder gespeichert sind, an
        Nach der Generierung der Videodatei wird das Verzeichnis, in dem die Bilder
        gespeichert sind, gelöscht
        param: path ... Pfad, worin die Bilder gespeichert sind
        param: filename ... Name der Ausgabedatei (mp4-Format empfohlen!)
        param: fps ... Frames per second (optional, 30 empfohlen)
        """
        self.generate_video_from_images(self.generate_image_list(path, fps), filename, fps)
        self.delete_directory(path)

# Main Programm
def __main__():
    # Definiere Bild Tuple mit Bilddauer (in Sekunden)
    #image_list = (["bild1.jpg", 1], ["bild2.jpg", 2], ["bild3.jpg", 1], ["bild4.jpg", 1], ["bild5.jpg", 3], ["bild6.jpg", 1], ["bild7.jpg", 0.5], ["bild8.jpg", 1], ["bild9.jpg", 1], ["bild10.jpg", 1])  # Hier gibt man die Pfade der Bilder an, die zum Video konvertiert werden sollen
    # Generiere Video aus dem Tuple

    #image_list = vg.generate_image_list(path="./proj", fps=2)
    #vg.generate_video_from_images(image_list, "output38.mp4")
    # vg.delete_directory("./proj")

    # bild1 für 3sek
    # diesenreiter bild1 -> bild2
    # bild2 für 3sek
    # duernberger bild2 -> schwarz


    # VideoGenerator Objekt wird angelegt
    vg = VideoGenerator()
    #vg.generate_video_from_path("./proj", "output.mp4") # Generiere Video
    vg.generate_video_from_path("./output_images", "duesen.mp4", fps=60) # Generiere Video

if __name__ == "__main__":
    __main__()