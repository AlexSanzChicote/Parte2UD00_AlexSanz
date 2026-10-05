from functools import reduce


# Lista de diccionarios componentes
Componentes = [
   {"nombre": "teclado", "precio": 25},
   {"nombre": "Raton", "precio": 5},
   {"nombre": "Ordenador", "precio": 2500},
   {"nombre": "Pantalla", "precio": 100}
]


# Buscar producto más barato con lambda
componenteBarato = min(Componentes, key=lambda x: x["precio"])
print(componenteBarato)


# Extraer los nombres de los componentes
ComponentesNombres = list(map(lambda x: x["nombre"], Componentes))
print(ComponentesNombres)


# Convertir la cadena en una lista de caracteres
UnicoAccesorio = "Alfombrilla"
print(list(UnicoAccesorio))


# Convertir a entero
numeroTexto = 3
numeroEntero = int(numeroTexto)
print(numeroEntero)


# Cadena de números a lista de enteros
CadenaNumeros = "1,12,3,14,15,6,17,8,19"
listaEnteros = list(map(int, CadenaNumeros.split(",")))
print(listaEnteros)


# Filtrar números mayores a 10 (convertimos a lista para imprimir los valores reales)
Uso_filter = list(filter(lambda x: x > 10, listaEnteros))
print(Uso_filter) # Imprime numeroa mayores a 10


# Multiplicar todos los números de la lista
Uso_reduce = reduce(lambda x, y: x * y, listaEnteros)
print(Uso_reduce) # Imprime la multiplicación de todos los números de la lista
