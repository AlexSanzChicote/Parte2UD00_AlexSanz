def es_palindromo(numero):
   """
   >>> es_palindromo(121)
   True
   >>> es_palindromo(123)
   False
   """
   texto = str(numero).strip()
   return texto == texto[::-1]




def es_primo(numero):
   """
   >>> es_primo(7)
   True
   >>> es_primo(4)
   False
   """
   try:
       n = int(numero)
   except ValueError:
       return False
   if n < 2:
       return False


   for i in range(2, n):
       if n % i == 0:
           return False
   return True


if __name__ == "__main__":
   #  Ejecutar los tests 
   import doctest
   resultado_tests = doctest.testmod()


   # Si los tests fallan, no continúa
   if resultado_tests.failed > 0:
       print("Error: Los tests unitarios no se han superado.")
   else:
       print("Tests unitarios superados correctamente.")


       # Pedir los nombres de los archivos por pantalla
       archivo_entrada = input("Introduce el nombre del archivo de entrada: ")
       archivo_salida = input("Introduce el nombre del archivo de salida: ")


       contador_palindromos = 0
       contador_primos = 0
       lista_ambos = []


       # Leer archivo de entrada
       with open(archivo_entrada, "r") as entrada:
           for linea in entrada:
               linea = linea.strip()
               if not linea:
                   continue


               numero = int(linea)


               es_pal = es_palindromo(numero)
               es_pri = es_primo(numero)


               if es_pal:
                   contador_palindromos += 1


               if es_pri:
                   contador_primos += 1


               if es_pal and es_pri:
                   lista_ambos.append(str(numero))


       # Escribir archivo de salida
       with open(archivo_salida, "w") as salida:
           salida.write(f"Hay {contador_palindromos} números palíndromos.\n")
           salida.write(f"Hay {contador_primos} números primos.\n")
           for n in lista_ambos:
               salida.write(f"{n}\n")


       print("Proceso completado correctamente.")


