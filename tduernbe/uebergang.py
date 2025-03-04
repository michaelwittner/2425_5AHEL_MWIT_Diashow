import cv2
import numpy as np  #cv2 und numpy importiert

image = cv2.imread(r"H:\MWIT\foto.jpg") #Bild einlesen
height, width, _ = image.shape  #Abmessungen auslesen

frames = 30 #Anzahl der Frames, die bearbeitet werden
fps = 60

for i in range(frames + 1): #Schleife mit der Anzahl der Frames, sodass für jeden Frame geschwärzt wird

    alpha = 1 - (i / frames) #Alphawert für addWeighted berechnet, siehe Tutorial
    darkened = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, 0) #Bild nach und nach schwärzen

    #https://docs.opencv.org/3.4/d5/dc4/tutorial_adding_images.html

    cv2.imshow("Übergang", darkened) #Bild ausgeben/anzeigen

    if cv2.waitKey(5) & 0xFF == ord('q'): #bei waitKey kann man die Wiederholungsrate in ms eintragen, hier 1, weil der Übergang schnell sein soll
        break

cv2.waitKey(0)  # Wartet unendlich, bis eine Taste gedrückt wird.
cv2.destroyAllWindows()

