import cv2
import numpy as np
# --leer la imagen
img = cv2.imread('src\A.png', 0)
# --elemento estructurante
kernel = np.ones((7, 7), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# --realizar la erosion
erosion = cv2.erode(img, kernel, iterations=1)
# --mostrar resultados
cv2.imshow("original", img)
cv2.imshow("erosion", erosion)
cv2.waitKey()
