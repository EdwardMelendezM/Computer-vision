import cv2
import numpy as np
# --leer imagen
image = cv2.imread('src/ave.jpg')
# --obtener dimensiones de la imagen
ancho = image.shape[1]  # columnas
alto = image.shape[0]  # filas
# --define la matriz de rotación
M = cv2.getRotationMatrix2D((ancho//2, alto//2), 15, 1)
# --ejecuta la rotación
imageOut = cv2.warpAffine(image, M, (ancho, alto))
# --muestra las imágenes
cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()
