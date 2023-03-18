import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer la imagen original
img = cv2.imread("src/marsrover.png")

# Obtener alto y ancho de la imagen
height = img.shape[0]
width = img.shape[1]

# Crear una imagen nueva
new_img = np.zeros((height, width, 3), np.uint8)

# Operación de cuantización de la imagen.
# El nivel de cuantización es 2
for i in range(height):
    for j in range(width):
        for k in range(3):  # Correspondiente a los componentes BGR
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 128
            new_img[i, j][k] = np.uint8(gray)

# Mostrar la imagen
cv2.imshow("src", img)
cv2.imshow("", new_img)

# Esperar
cv2.waitKey(0)
cv2.destroyAllWindows()
