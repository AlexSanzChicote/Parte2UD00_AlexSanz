

import ssl


# Desactivamos la verificación SSL para que EasyOCR pueda descargar los modelos sin error
ssl._create_default_https_context = ssl._create_unverified_context


import cv2
import easyocr
import matplotlib.pyplot as plt


# Lector indicando los idiomas que queremos buscar
lector = easyocr.Reader(['es', 'en'])


# Cargamos la imagen que queremos leer
ruta_imagen = 'imagen_ejemplo.png' 
imagen = cv2.imread(ruta_imagen)


if imagen is None:
   raise FileNotFoundError(f"No se pudo encontrar la imagen en la ruta: {ruta_imagen}")


# Leemos todo el texto que aparece en la imagen
resultados = lector.readtext(imagen)


# Mostramos en pantalla el texto encontrado y su porcentaje de seguridad
print(" Textos detectados en la imagen")
for (ubicacion, texto, seguridad) in resultados:
   print(f"- Texto leído: '{texto}' (Seguridad: {seguridad * 100:.0f}%)")
  
   # Cuadro verde alrededor del texto que hemos encontrado
   punto1 = (int(ubicacion[0][0]), int(ubicacion[0][1]))
   punto2 = (int(ubicacion[2][0]), int(ubicacion[2][1]))
   cv2.rectangle(imagen, punto1, punto2, (0, 255, 0), 2)


# Mostramos la imagen final con los recuadros verdes encima del texto
imagen_color_correcte = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
plt.imshow(imagen_color_correcte)
plt.axis('off')
plt.title("Resultado del reconocimiento de texto")
plt.show()
