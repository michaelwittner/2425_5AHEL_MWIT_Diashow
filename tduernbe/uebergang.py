import cv2
import numpy as np

image = cv2.imread(r"H:\MWIT\foto.jpg")
height, width, _ = image.shape

frames = 30
fps = 60

for i in range(frames + 1):

    alpha = 1 - (i / frames)
    darkened = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, 0)

    cv2.imshow("Übergang", darkened)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
