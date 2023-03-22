import cv2

# Cargar la imagen
image = cv2.imread('src/many fruits.png')
cv2.imshow('Imagen original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convertir a binario con un umbral adecuado
ret, binary_im = cv2.threshold(gray_image, 245, 255, cv2.THRESH_BINARY)

# Invertir la imagen
binary_im = ~binary_im

# Encontrar los contornos externos
contours, hierarchy = cv2.findContours(
    binary_im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos con diferentes colores según el tipo de fruta
for contour in contours:
    # Obtener el área y la posición del contorno
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    # Calcular la relación de aspecto
    aspect_ratio = w / h
    # Si la relación de aspecto está dentro de ciertos límites, se considera una manzana
    if 0.8 <= aspect_ratio <= 1.2:
        color = (0, 255, 0)  # Color verde
    # Si el área es grande y la relación de aspecto está dentro de ciertos límites, se considera una naranja
    elif area > 3000 and 0.5 <= aspect_ratio <= 0.8:
        color = (0, 0, 255)  # Color rojo
    # Si la relación de aspecto está dentro de ciertos límites, se considera un plátano
    else:
        color = (255, 0, 0)  # Color azul
    # Dibujar el rectángulo con el color correspondiente
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)

# Mostrar la imagen con los contornos marcados
cv2.imshow('Contornos marcados en la imagen RGB', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
