import cv2
# --leer imagen
image = cv2.imread('src/ave.jpg')
# --obtener dimensiones
ancho = image.shape[1]  # columnas
alto = image.shape[0]  # filas
print(alto, ancho)
# --escalando la imagen
imageOut = cv2.resize(image, (600, 300), interpolation=cv2.INTER_CUBIC)
# --mostrar las imágenes
cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()
