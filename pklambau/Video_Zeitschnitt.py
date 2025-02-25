import cv2

# Video-Datei öffnen
cap = cv2.VideoCapture("drift.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Beende die Wiedergabe, wenn das Video zu Ende ist

    cv2.imshow("Video", frame)

    # Warte auf eine Taste (1 ms), 'q' zum Beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
