import cv2
from PIL import Image


def video_generator_from_images(images: list, filename: str, fps: int = 30, height: int = None, width: int = None) -> None:
    """
    Erstellt ein Video aus einer Liste von Bildern.

    :param images: Liste von Bildpfaden
    :param filename: Name der Ausgabedatei (mp4-Format empfohlen)
    :param fps: Frames per Second (Standard: 30)
    :param width: Breite des Videos (Standard: None)
    :param height: Länge des Videos (Standard: None)
    """
    print("Generating video...")

    # Überprüfe, ob die Liste leer ist.
    if not images:
        print("Fehler: Keine Bilder in der Liste!")
        return

    # Laden des ersten Bildes, um die Videogröße zu bestimmen
    first_image = Image.open(images[0])

    # Überprüfe, ob height und width Parameter angegeben wurden
    if height and width is None:
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
    for img_path in images:
        # Lade das Bild
        img = cv2.imread(img_path)
        # Überprüfe, ob Bild geladen wurde
        if img is None:
            print(f"Warnung: Bild {img_path} konnte nicht geladen werden und wird übersprungen.")
            continue

        # Falls notwendig, Bildgröße anpassen
        img = cv2.resize(img, (width, height))
        # In das Video schreiben
        video.write(img)

    # Schließe Videofile
    video.release()
    print(f"Video erfolgreich erstellt: {filename}")


# Beispielhafte Nutzung
def __main__():
    image_list = ["bild1.jpg", "bild2.jpg", "bild3.jpg", "bild4.jpg", "bild5.jpg", "bild6.jpg", "bild7.jpg", "bild8.jpg","bild9.jpg", "bild10.jpg"]  # Hier gibt man die Pfade der Bilder an, die zum Video konvertiert werden sollen
    # image_list = [["bild1.jpg", 1], "bild2.jpg", "bild3.jpg", "bild4.jpg", "bild5.jpg", "bild6.jpg", "bild7.jpg", "bild8.jpg","bild9.jpg", "bild10.jpg"]  # Hier gibt man die Pfade der Bilder an, die zum Video konvertiert werden sollen
    video_generator_from_images(image_list, "output_video.mp4", fps=3)


if __name__ == "__main__":
    __main__()