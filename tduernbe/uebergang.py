import cv2
import numpy as np  # OpenCV und NumPy für Bildverarbeitung importieren

# Die Funktion uebergang erstellt eine Bildsequenz, die einen Übergangseffekt simuliert, indem ein gegebenes Bild schrittweise in eine gewählte Zielfarbe übergeht.
# Dies geschieht durch eine lineare Reduzierung der Alpha-Werte, sodass das Bild allmählich mit der Zielfarbe überblendet wird.
# Die Anzahl der Frames, die diesen Übergang ausmachen, wird durch die gewählte Übergangszeit (zeit_uebergang) und die Framerate (fps) bestimmt.
# Alle generierten Bilder werden in einem definierten Zielordner gespeichert.
# Alle Bilder müssen gleich groß sein.
# Die Farbe kann einfach mit der zielfarbe gewählt werden, einfach RGB-Wert eintragen

def uebergang(bild_pfad, ziel_ordner, zeit_uebergang, fps, zielfarbe=(0, 0, 0)):
    """
     Erzeugt eine Sequenz von Bildern mit einem allmählichen Übergang in eine gewählte Zielfarbe.

     :param bild_pfad: Pfad zum Ausgangsbild
     :param ziel_ordner: Zielverzeichnis zur Speicherung der generierten Bilder
     :param zeit_uebergang: Dauer des Übergangs in Sekunden
     :param fps: Anzahl der Frames pro Sekunde
     :param zielfarbe: RGB-Tupel für die Farbe, in die übergeblendet werden soll (Standard: Schwarz)
     :return: Liste mit den Namen der generierten Bilder
     """

    bildliste = []

    # Bild einlesen
    image = cv2.imread(bild_pfad)
    if image is None:
        raise FileNotFoundError(f"Das Bild unter {bild_pfad} konnte nicht geladen werden.")  # Fehler, falls das Bild nicht auf dem Pfad liegt

    height, width, _ = image.shape  # Abmessungen des Bildes auslesen

    # Anzahl der Frames für den Übergang berechnen
    frames = int(fps * zeit_uebergang)

    # Zielfarbe als Bild mit den gleichen Abmessungen wie das Originalbild erstellen
    zielfarbe_bild = np.full_like(image, zielfarbe, dtype=np.uint8)

    for i in range(frames):
        alpha = 1 - (i / frames)  # Alphawert berechnen (von 1 bis 0 für den Übergang)
        # Alpha reduziert sich schrittweise auf 0, sodass das Bild langsam in die Zielfarbe übergeht

        # Bildübergang durch gewichtete Addition mit der Zielfarbe
        blended = cv2.addWeighted(image, alpha, zielfarbe_bild, 1 - alpha, 0)

        # Dateiname für den aktuellen Frame generieren
        frame_name = f"{ziel_ordner}/blende_{str(i + 1).zfill(3)}.jpg"

        # Bild speichern und prüfen, ob der Vorgang erfolgreich war
        if not cv2.imwrite(frame_name, blended):  # Überlagert Bilder mit dem Transparenzeffekt
            raise FileNotFoundError("Zielordner existiert nicht oder ist nicht beschreibbar.")

        # Dateinamen der Liste hinzufügen
        bildliste.append(frame_name)

    return bildliste
