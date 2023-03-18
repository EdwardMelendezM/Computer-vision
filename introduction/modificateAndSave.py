import cv2
# Dirección de la imagen
image_path = "src/marsrover.png"
# Leer la imagen
image = cv2.imread(image_path)
# set the start and end coordinates
# Establecer coordenadas iniciales y finales
# de la esquina sup. izq. y de inf. der. del rectángulo
start = (100, 70)
end = (350, 380)
# Establecer el color y el grosor de los bordes
color = (0, 255, 0)
thickness = 30
# Dibujar el rectángulo
cv2.rectangle(image, start, end, color, thickness)
# Grabar la imagen modificada son el rectángulo dibujado
cv2.imwrite("rectangle.jpg", image)
# Mostrar la imagen modificada
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
