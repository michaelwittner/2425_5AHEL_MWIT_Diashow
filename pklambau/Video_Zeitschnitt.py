import cv2

cap = cv2.VideoCapture("video.mp4")  # Video-Datei öffnen

if not cap.isOpened():  # Überprüfen, ob das Video erfolgreich geöffnet wurde
    print("Fehler: Video konnte nicht geöffnet werden")  # Fehler ausgeben, falls das Öffnen fehlschlägt
    exit()  # Programm beenden

while cap.isOpened():  # Solange das Video geöffnet ist, wiederhole die Schleife
    ret, frame = cap.read()  # Nächstes Frame aus dem Video lesen

    if not ret:  # Falls kein weiteres Frame gelesen werden kann (Video zu Ende oder Fehler)
        break  # Schleife beenden

    cv2.imshow("Video", frame)  # Das aktuelle Frame im Fenster anzeigen

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Warten (1ms) auf eine Taste, falls 'q' gedrückt wird
        break  # Schleife beenden und Video stoppen

cap.release()  # Freigabe der Videoressourcen
cv2.destroyAllWindows()  # Alle OpenCV-Fenster schließen
