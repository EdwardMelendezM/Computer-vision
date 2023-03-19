import cv2
import matplotlib.pyplot as plt
# --leer la imagen
img = cv2.imread("src/sunflower.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('grayscale image', img)
# --calcular el histograma, por defecto 10 bins
plt.hist(img.ravel())
plt.show()
# --esperar
cv2.waitKey(0)
cv2.destroyAllWindows()
