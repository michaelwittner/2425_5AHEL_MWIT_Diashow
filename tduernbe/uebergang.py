import cv2
import numpy as np  #cv2 und numpy importiert

# Die Funktion uebergang erstellt eine Bildsequenz, die einen Übergangseffekt simuliert, indem ein gegebenes Bild schrittweise abdunkelt.
# Dies geschieht durch eine lineare Reduzierung der Alpha-Werte, sodass das Bild allmählich in Schwarz übergeht. Die Anzahl der Frames,
# die diesen Übergang ausmachen, wird durch die gewählte Übergangszeit (zeit_uebergang) und die Framerate (fps) bestimmt.
# Alle generierten Bilder werden in einem definierten Zielordner gespeichert.
# Alle Bilder müssen gleich groß sein.

def uebergang(bild_pfad, ziel_ordner, zeit_uebergang, fps):
    """
     Erzeugt eine Sequenz von Bildern mit einem allmählichen Abdunklungseffekt.

     :param bild_pfad: Pfad zum Ausgangsbild
     :param ziel_ordner: Zielverzeichnis zur Speicherung der generierten Bilder
     :param zeit_uebergang: Dauer des Übergangs in Sekunden
     :param fps: Anzahl der Frames pro Sekunde
     :return: Liste mit den Namen der generierten Bilder
     """

    bildliste = []

    # Bild einlesen
    image = cv2.imread(bild_pfad)
    if image is None:
        raise FileNotFoundError(f"Das Bild unter {bild_pfad} konnte nicht geladen werden.")  #Fehler, falls das Bild nicht auf dem Pfad liegt

    height, width, _ = image.shape  # Abmessungen des Bildes auslesen

    # Anzahl der Frames für den Übergang berechnen
    frames = int(fps * zeit_uebergang)

    for i in range(frames):
        alpha = 1 - (i / frames)  # Alphawert berechnen (von 1 bis 0 für das Abdunkeln)
        #Alpha reduziert sich schrittweise auf 0, sodass das Bild langsam in Schwarz übergeht

        # Bild abdunkeln durch gewichtete Addition mit einer schwarzen Maske
        darkened = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, 0)

        # Dateiname für den aktuellen Frame generieren
        frame_name = f"{ziel_ordner}/blende_{str(i + 1).zfill(3)}.jpg"

        # Bild speichern und prüfen, ob der Vorgang erfolgreich war
        if not cv2.imwrite(frame_name, darkened): #Überlagert Bilder mit dem Transparenzeffekt
            raise FileNotFoundError("Zielordner existiert nicht oder ist nicht beschreibbar.")

        # Dateinamen der Liste hinzufügen
        bildliste.append(frame_name)

    return bildliste
