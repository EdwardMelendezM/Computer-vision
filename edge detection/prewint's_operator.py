import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# --Leer la imagen
img = cv.imread('src/mary.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# --convertir a escala de grises
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# --Operador de Prewitt
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)

x = cv.filter2D(grayImage, cv.CV_16S, kernelx)
y = cv.filter2D(grayImage, cv.CV_16S, kernely)
# --Convertir a uint8, y fusionar la imagen
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
# --Mostrar las imagenes
titles = ['Imagen original', 'Operador de Prewitt']
images = [rgb_img, Prewitt]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
