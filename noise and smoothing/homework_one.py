# -- Importamos las librerias
# para manejar imagenes y videos
import cv2
import cv2 as cv
# Arreglos y operaciones numericas
import numpy as np
# Graficas
from matplotlib import pyplot as plt

# Cargar la imagen de Lena con Ruido
img = cv.imread('src/lena_ruido.jpg')
# Usamos el metodo de .blur para el filtro
blur = cv.blur(src=img, ksize=(31, 31))

# Mostramos Resultados
plt.subplot(121), plt.imshow(img), plt.title('Lena con Ruido')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Lena con Filtro ')
plt.xticks([]), plt.yticks([])
plt.show()


# cargar las imágen
img2 = cv2.imread("src/lena_ruido.jpg", 1)
# Creando un filtrado promedio(Kernel)
filter = np.array([[1/(31**2) for i in range(31)] for j in range(31)])
# Aplicando la función cv2.filter2D en la imagen
sharpen_img_2 = cv2.filter2D(img2, -1, filter)
cv2.imshow("lena rruido", img2)
cv2.imshow("lena filtro", sharpen_img_2)
cv2.waitKey(0)


# Reading an image in default mode
image = cv2.imread("src/lena.jpg")

# Window name in which image is displayed
window_name = 'Image'

# ksize
ksize = (30, 30)

# Using cv2.blur() method
image = cv2.blur(image, ksize)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
