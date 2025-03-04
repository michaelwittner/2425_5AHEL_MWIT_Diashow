import cv2
from PIL import Image

# VideoGenerator Klasse
class VideoGenerator:
    # Konstruktor der VideoGenerator Klasse
    def __init__(self):
        print("Video Generator")

    # Definiere Methode
    def generate_video_from_images(self, images: tuple, filename: str, fps: int = 30, height: int = None,
                                   width: int = None, codec: str = "mp4v") -> None:
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
        print("Codec:", codec)

        # Überprüfe, ob die Liste leer ist.
        if not images:
            print("Fehler: Keine Bilder in der Liste!")
            return

        # Laden des ersten Bildes, um die Videogröße zu bestimmen
        first_image = Image.open(images[0][0])

        # Überprüfe, ob height und width Parameter angegeben wurden
        if height is None and width is None:
            widthVideo, heightVideo = first_image.size
        else:
            widthVideo = width
            heightVideo = height

        # OpenCV VideoWriter initialisieren
        # Audiocodec definieren
        fourcc = cv2.VideoWriter_fourcc(*codec)  # Codec für MP4-Format
        # Initialisiere Video(-Writer)
        video = cv2.VideoWriter(filename, fourcc, fps, (widthVideo, heightVideo))

        # for Schleife über die Bilder
        for img_path, duration in images:
            # Lade das Bild
            img = cv2.imread(img_path)
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
def main():
    # Definiere Bild Tuple mit Bilddauer (in Sekunden)
    image_list = (["bild1.jpg", 1], ["bild2.jpg", 2], ["bild3.jpg", 1], ["bild4.jpg", 1], ["bild5.jpg", 3], ["bild6.jpg", 1], ["bild7.jpg", 0.5], ["bild8.jpg", 1], ["bild9.jpg", 1], ["bild10.jpg", 1])  # Hier gibt man die Pfade der Bilder an, die zum Video konvertiert werden sollen
    # Generiere Video aus dem Tuple
    vg = VideoGenerator()
    vg.generate_video_from_images(image_list, "output10.mp4")

    # Folgende Codecs gelten für folgende Formate:
    # Format: mp4 Codecs: mp4v, h264, avc1
    # Format: avi Codecs: fmp4, xvid, mjpg, mp4v
    # Format: mkv Codecs: h264, vp80, vp90, avc1
    # Format: mov Codecs: h264, mjpg, mp4v
    # Format: webm Codecs: vp80, vp90
    # Format: flv Codecs: h264, flv1
    # Format: wmv Codecs: wmv1, wmv2, wmv3

if __name__ == "__main__":
    main()
