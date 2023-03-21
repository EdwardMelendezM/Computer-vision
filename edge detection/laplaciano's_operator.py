import cv2 as cv
import matplotlib.pyplot as plt
# --Leer la iamgen
img = cv.imread('src/mary.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# --Convertir a escala de grises
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# --Operador Laplaciano
dst = cv.Laplacian(grayImage, cv.CV_16S, ksize=3)
Laplacian = cv.convertScaleAbs(dst)
# --Mostrar imagenes
titles = ['Imagen original', 'Operador Laplaciano']
images = [rgb_img, Laplacian]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
