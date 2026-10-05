# Lista de patrones a buscar
patrones = ["00", "101", "ABC", "HO"]


def numeroPatrones(text):
   text = text.upper()
   numero_patrones = 0
   no_patron = 0
  
   i = 0
   while i < len(text):
       encontrado = False
      
       # Comprobamos si en la posición actual empieza algún patrón o su opuesto
       for patron in patrones:
           patron_opuesto = patron[::-1]
           longitud = len(patron)
          
           # Subcadena actual del tamaño del patrón
           subcadena = text[i : i + longitud]
          
           if subcadena == patron or subcadena == patron_opuesto:
               numero_patrones += 1
               i += longitud  # Saltamos el patrón completo encontrado
               encontrado = True
               break
      
       # Si en esta posición no encuentra ningún patron, suma 1
       if not encontrado:
           no_patron += 1
           i += 1


   print(f"Patrones encontrados: {numero_patrones}")
   print(f"Elementos que NO son patrón: {no_patron}")
  
   return numero_patrones


# Programa principal
cadenaTexto = input("Introduce una cadena de texto: ")
numeroPatrones(cadenaTexto)


