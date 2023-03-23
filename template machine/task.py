from __future__ import print_function
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse


def CambiarTamaño(image, width=None, height=None, inter=cv2.INTER_AREA):
    # inicializar las dimensiones de la imagen que se cambiará de tamaño y
    # toma el tamaño de la imagen
    dim = None
    (h, w) = image.shape[:2]

    # si tanto el ancho como el alto son None, entonces devuelve la
    # imagen original
    if width is None and height is None:
        return image

    # compruebe si el ancho es None
    if width is None:
        # calcular la relación de la altura y construir las
        # dimensiones
        r = height / float(h)
        dim = (int(w * r), height)

    # de lo contrario, la altura es None
    else:
        # calcular la relación del ancho y construir las
        # dimensiones
        r = width / float(w)
        dim = (width, int(h * r))

    # cambiar el tamaño de la imagen
    resized = cv2.resize(image, dim, interpolation=inter)

    # devolver la imagen redimensionada
    return resized


def RotarImagen(image, angulo):
    # Obteniendo las imensiones de la imagen
    rows, cols, channels = image.shape
    # Obtener los aparametros de rotacion
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angulo, 1)
    # rotar la imagen dado el angulo
    rotate = cv2.warpAffine(image, M, (cols, rows))
    # devolver la imagen rotada
    return rotate


def BajarSubirBrillo(image, gamma=1.0):
    # construir una tabla de búsqueda mapeando los valores de píxel [0, 255] a
    # sus valores gamma ajustados
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # aplicar la corrección gamma usando la tabla de búsqueda
    return cv2.LUT(image, table)


def match_template(image, template):
    '''Funcion: permite el emparejamiento de plantillas 
       para encontrar una plantilla en una imagen mediante 
       los metodos de coincidencia disponibles de OpenCV
       Input: 
         * image   : imagen de origen 
         * template: imagen de plantilla
       Output:
         * area y posicion de coincidencia mas alta  
        '''
    # --convertir las imagenes de BGR a RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

    # -- mostrar las imagenes
    plt.imshow(image)
    plt.imshow(template)
    # --dimensiones de la plantilla
    template.shape
    # --lista con los nombres de diferentes métodos de coincidencia de plantillas.
    methods = ["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR",
               "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"]

    # --obtener los resultados para cada metodo
    for m in methods:
        #
        img_copy = image.copy()
        method = eval(m)
        # comparamos las imagenes T y I con la funcion cv2.matchTemplate
        # res: es  la matriz resultante
        res = cv2.matchTemplate(img_copy, template, method)
        # recuperamos el valor minimo y maximo(min_val, max_val)
        # recuperacoms sus ubicaciones(min_loc, max_loc)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Si los metodos son cv2.TM_SQDIFF y cv2.TM_SQDIFF_NORMED
        # entonces tendremos que encontrar el valor mas bajo(mejor emparejamiento)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        print("Loc mejor emparejamiento:", top_left)
        # definicmos los puntos x1, y1 y x2, y2
        # que nos ayudarán a dibujar un rectángulo.
        height, width, channels = template.shape
        bottom_right = (top_left[0]+width, top_left[1]+height)
        # dibujamos el rectangulo con los puntos
        cv2.rectangle(img_copy, top_left, bottom_right, (0, 255, 0), 6)
        # Mostramos resultados
        plt.subplot(121)
        plt.imshow(res)
        plt.title("TEMPLATE MATCHING MAP")
        plt.subplot(122)
        plt.imshow(img_copy)
        plt.title("TEMPLATE DETECTION")
        plt.suptitle(m)
        plt.show()
        print("\n")


# Imagen de Messi
img = cv2.imread("image1.jpg")


# Cambio de tamaño la imagen de Messi
image_cambio_tamaño = CambiarTamaño(
    img, width=1026, height=768, inter=cv2.INTER_AREA)


# Rotamos la imagen de Messi
imagen_rotada = RotarImagen(image=img, angulo=15)


# Cambiamos el brillo
imagen_oscura = BajarSubirBrillo(img, gamma=0.4)

# --------------------------------------------------------------
# leemos el template
template = cv2.imread("template1.jpg")

# ------ AQUI PROBAMOS CON EL TAMAÑO ------
match_template(image=image_cambio_tamaño, template=template)

# ------ AQUI PROBAMOS CON EL ROTAMIENTO ------
match_template(image=imagen_rotada, template=template)

# ------ AQUI PROBAMOS CON EL ROTAMIENTO ------
match_template(image=imagen_oscura, template=template)

# Como se puede observar el algoritmo de Template matching no suele ser muy robusto ante el aspecto del cambio de tamanio la rotacion o el oscurecimeintod e las imagenes(a menos que tanto la imagen I, como el template presenten las mismas condiciones). Podríamos experimentar uesto resalizando los siguientes experimentos
