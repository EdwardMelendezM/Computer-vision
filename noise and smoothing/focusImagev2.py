import cv2
import numpy as np
# cargar las imágenes
img1 = cv2.imread("src/lena.jpg", 1)
# Creando el filtro de sombrero mexicano
filter = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0],
                  [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])
# Aplicando la función cv2.filter2D
mexican_hat_img1 = cv2.filter2D(img1, -1, filter)
cv2.imshow("cat con filtro", mexican_hat_img1)

img2 = cv2.imread("src/marsrover.png", 1)
# Creando el filtro de sombrero mexicano
filter = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -
                                                                                1, -2, -1, 0], [0, 0, -1, 0, 0]])
# Aplicando la función cv2.filter2D
mexican_hat_img2 = cv2.filter2D(img2, -1, filter)
cv2.imshow("lena con filtro", mexican_hat_img2)
cv2.waitKey(0)
