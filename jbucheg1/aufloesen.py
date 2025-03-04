from PIL import Image
import numpy as np
import random
import os
import matplotlib.pyplot as plt

# Bilder laden
image1 = Image.open('foto.jpg')
image2 = Image.open('foto2.jpg')

# Sicherstellen, dass beide Bilder die gleiche Größe haben
image1 = image1.resize(image2.size)

# Konvertiere beide Bilder in RGBA (einschließlich Alpha-Kanal für Transparenz)
image1 = image1.convert("RGBA")
image2 = image2.convert("RGBA")

# Bilder als NumPy Arrays umwandeln
image1_array = np.array(image1)
image2_array = np.array(image2)

# Bildgröße
height, width, _ = image1_array.shape

# Anzahl der Bilder, die gespeichert werden sollen
num_images = 10  # Anzahl der Bilder, die du speichern möchtest

# Berechne die Anzahl der benötigten Blöcke, um genau num_images Bilder zu speichern
# Der Blockbereich ist ein Quadrat, also wird die Wurzel der Anzahl der Bilder genommen
num_blocks_per_side = int(np.ceil(np.sqrt(num_images)))  # Berechnet die Seitenlänge des Blocks

# Berechne die Blockgröße
block_size = min(width, height) // num_blocks_per_side

# Zufällige Reihenfolge der Blöcke generieren
blocks = [(x, y) for x in range(0, width, block_size) for y in range(0, height, block_size)]
random.shuffle(blocks)

# Stellen sicher, dass die Liste nur die Anzahl der gewünschten Bilder enthält
blocks = blocks[:num_images]

# Ordner zum Speichern der Bilder erstellen (falls nicht bereits vorhanden)
output_dir = 'output_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Übergangseffekt (die Blöcke werden nach und nach transparent)
fig, ax = plt.subplots()

# Iteriere über die Schritte und mache den Übergang
for step_idx, (x, y) in enumerate(blocks):
    # Kopiere das Bild 1 und setze den aktuellen Block transparent
    img_with_alpha = np.copy(image1_array)

    # Setze den Block transparent
    img_with_alpha[y:y+block_size, x:x+block_size, 3] = 0  # Alpha-Kanal auf 0 setzen (transparent)

    # Kombiniere das Bild mit dem transparenten Block und Bild 2
    blended_image = np.copy(img_with_alpha)
    # Kombiniere Bild 2, wo das Bild 1 transparent ist
    mask = img_with_alpha[:, :, 3] == 0
    blended_image[mask] = image2_array[mask]

    # Speichere das Bild
    output_path = os.path.join(output_dir, f'output_{step_idx:04d}.png')
    Image.fromarray(blended_image).save(output_path)

    # Optional: Zeige das Bild in der Matplotlib-Ansicht
    ax.clear()
    ax.imshow(blended_image)
    ax.axis('off')
    plt.pause(0.05)  # Kurze Pause zwischen den Bildern für flüssigere Animation

plt.show()
