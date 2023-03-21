# Importamos los modulos requeridos
import cv2
import numpy as np
import matplotlib.pyplot as plt
# -- Leemos las imagenes
img1 = cv2.imread("src/board1.jpg")
img2 = cv2.imread("src/board2.jpg")
# -- convertimos a escala de grises
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Establecer umbral y valor máximo
thresh = 150
maxValue = 255
# Umbral binario
th, dst1 = cv2.threshold(img1, thresh, maxValue, cv2.THRESH_BINARY)
# Umbral binario
th, dst2 = cv2.threshold(img2, thresh, maxValue, cv2.THRESH_BINARY)
# redimensionamos el tamaño de las imagenes
dst1 = cv2.resize(dst1, (400, 400), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(dst2, (400, 400), interpolation=cv2.INTER_AREA)
# Aplicando bitwise_xor bit a bit
dst = cv2.bitwise_xor(dst1, dst2)
# Mostramos resultado
plt.imshow(dst, cmap='gray')
plt.show()
