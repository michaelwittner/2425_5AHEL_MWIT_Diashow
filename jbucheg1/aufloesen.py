import math
import random
import cv2


image = cv2.imread('foto.JPG', cv2.IMREAD_UNCHANGED) # Bild laden
height = 600
width = 600
image = cv2.resize(image, (width, height)) # width und height festlegen
cv2.imshow('Originalbild', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Prüfen, ob das Bild einen Alpha-Kanal hat, wenn nicht, füge einen hinzu
if image.shape[2] == 3:
    # Alpha-Kanal hinzufügen
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

auflösung = 10
blockSize = math.ceil(width/auflösung),math.ceil(height/auflösung) # größe der einzelnen blöcke,

# Erstelle eine Liste mit allen möglichen Koordinaten (als Tupel)
alle_koordinaten = [(x, y) for x in range(auflösung) for y in range(auflösung)]

# Liste der bereits ausgewählten Koordinaten
ausgewaehlte_koordinaten = []

# Funktion, um eine zufällige Koordinate auszuwählen, die noch nicht ausgewählt wurde
def zufaellige_koord():
    # Stelle sicher, dass es noch unerwünschte Koordinaten gibt
    if len(ausgewaehlte_koordinaten) < len(alle_koordinaten):
        while True:
            # Wähle zufällig eine Koordinate
            koord = random.choice(alle_koordinaten)
            if koord not in ausgewaehlte_koordinaten:
                ausgewaehlte_koordinaten.append(koord)
                return koord
    else:
        return None  # Alle Koordinaten wurden bereits ausgewählt

for i in range(auflösung*auflösung):
    x,y = zufaellige_koord()
    x=x*blockSize[0]
    y=y*blockSize[1]
    image[y:y + blockSize[1], x:x + blockSize[1], 3] = 0

cv2.imshow('Bild', image)
cv2.waitKey(0)
cv2.imwrite('Bild.jpg', image)  #gif wird gebraucht
cv2.destroyAllWindows()
