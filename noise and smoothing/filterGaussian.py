import cv2
import numpy
# leer imagen
src = cv2.imread('src/lena.jpg', cv2.IMREAD_UNCHANGED)
# aplicar el filtro gaussiano
dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
# mostrar la imagen original y la imagen fikltrada
cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
