import cv2

def resize_image(image, max_width=640, max_height=320):
    # Obtener las dimensiones actuales de la imagen
    height, width = image.shape[:2]

    # Calcular el factor de escala para ajustar la imagen dentro del límite máximo
    scale_factor = min(max_width / width, max_height / height)

    # Calcular las nuevas dimensiones manteniendo la proporción
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Redimensionar la imagen usando cv2.resize
    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image