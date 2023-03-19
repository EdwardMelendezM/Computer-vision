import cv2
import numpy as np
from matplotlib import pyplot as plt
# --leer la imagen
img = cv2.imread('src/lena.jpg')
cv2.imshow('lena.jpg', img)
color = ('b', 'g', 'r')
# --calcular el histograma
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
