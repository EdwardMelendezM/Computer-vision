import cv2 as cv
import matplotlib.pyplot as plt
# --Leer la imagen
img = cv.imread('src/mary.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# --Convertir a escala de grises
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# --Operador de Sobel
x = cv.Sobel(grayImage, cv.CV_16S, 1, 0)
y = cv.Sobel(grayImage, cv.CV_16S, 0, 1)
# --Convertir a uint8, fusionar la imagen
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
# --Mostrar las imagenes
titles = ['Imagen original', 'Operador de Sobel']
images = [rgb_img, Sobel]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
