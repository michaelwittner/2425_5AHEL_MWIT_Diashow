import cv2
import numpy as np





def diagonal_blend(image1_path, image2_path, steps=100):
    # Bilder laden
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        print("Fehler: Ein oder beide Bilder konnten nicht geladen werden.")
        return

    # Größe anpassen, falls unterschiedlich
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    height, width, _ = img1.shape

    for i in range(steps + 1):
        mask = np.zeros((height, width), dtype=np.float32)
        diag_position = int((i / steps) * (width + height))

        for y in range(height):
            for x in range(width):
                if x + y < diag_position:
                    mask[y, x] = 1.0

        blended = (img1 * (1 - mask[:, :, np.newaxis]) + img2 * (mask[:, :, np.newaxis])).astype(np.uint8)

        cv2.imshow('Diagonal Blende', blended)
        cv2.waitKey(30)

    cv2.destroyAllWindows()


# Beispielaufruf mit Bildnamen
diagonal_blend('bild1.jpg', 'bild2.jpg')