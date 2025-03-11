import cv2
import numpy as np  #cv2 und numpy importiert


def uebergang(bild_pfad, ziel_ordner, zeit_uebergang, fps):

    image = cv2.imread(bild_pfad) #Bild einlesen
    height, width, _ = image.shape  #Abmessungen auslesen

    frames = int(fps * zeit_uebergang) # Frames berechnen weil Wittner sagt zeitübergang soll gewählt werden können

    for i in range(frames):
        alpha = 1 - (i / frames)   #alphawert berechnen      https://stackoverflow.com/questions/1962795/how-to-get-alpha-value-of-a-png-image-with-pil
        darkened = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, 0)
            # #https://docs.opencv.org/3.4/d5/dc4/tutorial_adding_images.html

        frame_name = ziel_ordner + "/blende_" + str(i + 1).zfill(3) + ".jpg"
        cv2.imwrite(frame_name, darkened) # Datei speichern


