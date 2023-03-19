import cv2 as cv
# leyendo la imagen cuyo ruido se eliminará usando la función imread()

imageread = cv.imread('src/lena.jpg')
# usando la función medianBlur() para eliminar el ruido de la imagen dada
imagenormal = cv.medianBlur(imageread, 5)
# mostrando la imagen sin ruido como la salida en la pantalla
cv.imshow('original:', imageread)
cv.imshow('Noiseless_image', imagenormal)
cv.waitKey(0)
cv.destroyAllWindows()
