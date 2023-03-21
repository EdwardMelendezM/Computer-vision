import cv2
# --leer la imagen
image = cv2.imread('src/ave.jpg')
# --recortar una imagen
imageOut = image[60:220, 280:480]
# --mostra las imágenes
cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()
