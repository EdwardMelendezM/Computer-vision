import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# --leer la imagen
img = cv.imread('src/mary.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# convertirlo a escala de grises
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# -- operador de Roberts
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
x = cv.filter2D(grayImage, cv.CV_16S, kernelx)
y = cv.filter2D(grayImage, cv.CV_16S, kernely)
# convertir a uint8, fusionar la imagen
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Roberts = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
# --mostrar los gráficos

titles = ['Imagen original', 'Operador de Roberts']
images = [rgb_img, Roberts]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
