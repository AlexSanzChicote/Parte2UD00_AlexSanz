def contandoMinas(campo):
   filas = len(campo)
   columnas = len(campo[0])


   resultado = []


   for i in range(filas):
       nuevaFila = []
       for x in range(columnas):


           # Si hay mina, se queda en -1
           if campo[i][x] == -1:
               nuevaFila.append(-1)
           else:
               contadorMinas = 0


               # Aquí se miran las posiciones de alrededor
               for fila_conjunta in range(i - 1, i + 2):
                   for columna_conjunta in range(x - 1, x + 2):


                       # añadir límite superior                        if 0 <= fila_conjunta < filas and 0 <= columna_conjunta < columnas:
                           if campo[fila_conjunta][columna_conjunta] == -1:
                               contadorMinas += 1


               nuevaFila.append(contadorMinas)
              
       resultado.append(nuevaFila)
   return resultado
          


campo = [
   [ 0, -1,  0,  0],
   [ 0,  0, -1,  0],
   [-1,  0,  0,  0]
]


tablero_resuelto = contandoMinas(campo)


# Mostramos el resultado
for fila in tablero_resuelto:
   print(fila)

