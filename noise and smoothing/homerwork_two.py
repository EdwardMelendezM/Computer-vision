import cv2
import numpy as np
from skimage.util import random_noise

# cargar la imagen
img = cv2.imread("src\insta.jpg")
cv2.imshow('sin ruido - Original', img)

# agregar diferentes tipos de ruido a la imagen
noise_gaussiano = random_noise(img, mode='gaussian', clip=True)
noise_sal_pimienta = random_noise(img, mode='s&p', amount=0.1)

# Las funciones anteriores devuelven una imagen de punto flotante
# en el rango de [0,1], los cambiamos a 'uint8'
# y de [0,255]

noise_gaussiano = np.array(255*noise_gaussiano, dtype='uint8')
noise_sal_pimienta = np.array(255*noise_sal_pimienta, dtype='uint8')


# Filtrado promedio
imagGaussiano = cv2.blur(noise_gaussiano, (5, 5))
imagSalPimienta = cv2.blur(noise_sal_pimienta, (5, 5))


# Filtro del ruido Gussiano y pimienta y sal
imagGaussiano = cv2.GaussianBlur(noise_gaussiano, (5, 5), cv2.BORDER_DEFAULT)
imagSalPimienta = cv2.GaussianBlur(
    noise_sal_pimienta, (5, 5), cv2.BORDER_DEFAULT)

# Filtrado bilateral gaussiano y salt and pepper
imagGaussiano = cv2.bilateralFilter(noise_gaussiano, -1, 5, 5)
imagSalPimienta = cv2.bilateralFilter(noise_sal_pimienta, -1, 5, 5)


# mostrar el filtro del ruido Gussiano
cv2.imshow('imagGaussiano', imagGaussiano)
# mostrar el filtro del ruido Sal y Pimienta
cv2.imshow('imagSalPimienta', imagSalPimienta)
cv2.waitKey(0)


# ¿Qué tipo de filtro funciona mejor en cada uno de los casos anteriores? Justifica tu respuesta-
# El filtro de la mediana es mejor para el ruido de sal y pimineta porque mejora la imagen y realiza un suavisado mucho mejor que los otros metodos de filtrado, ademas de ello eliminaalos detalles finos de las lineas, y eliina casi perfectamente el ruido de la imagen

# Para la imagen con ruido gaussiano se observa que el filtro gaussiano es un poco mejor en calidad de imagen, suavisado y desenfoque que el filtro medio.
