sudoku_valido = (
    "5 3 4 6 7 8 9 1 2\n"
    "6 7 2 1 9 5 3 4 8\n"
    "1 9 8 3 4 2 5 6 7\n"
    "8 5 9 7 6 1 4 2 3\n"
    "4 2 6 8 5 3 7 9 1\n"
    "7 1 3 9 2 4 8 5 6\n"
    "9 6 1 5 3 7 2 8 4\n"
    "2 8 7 4 1 9 6 3 5\n"
    "3 4 5 2 8 6 1 7 9\n"
)
with open("Sudoku.in", "w") as archivo_creado:
    archivo_creado.write(sudoku_valido)


def esSudokuCorrecto(miArrayBi):
    # Comprueba que cada fila contenga los numeros
    for fila in miArrayBi:
        if sorted(fila) != list(range(1, 10)):
            return False

    # Comprueba que cada columna contenga los numeros
    for c in range(9):
        columna = [miArrayBi[f][c] for f in range(9)]
        if sorted(columna) != list(range(1, 10)):
            return False

    # Comprueba que cada bloque de 3x3 contenga los numeros
    for f in range(0, 9, 3):
        for c in range(0, 9, 3):
            bloque = [miArrayBi[f+i][c+j] for i in range(3) for j in range(3)]
            if sorted(bloque) != list(range(1, 10)):
                return False

    return True


# Lee el tablero directamente del archivo
matriz = []
with open("Sudoku.in", "r") as archivo:
    for linea in archivo:
        if linea.strip():
            matriz.append([int(n) for n in linea.split()])

# Muestra el contenido del Sudoku por pantalla
print("Sudoku:")
for fila in matriz:
    print(*fila)

print()  # Linea en blanco para separar
