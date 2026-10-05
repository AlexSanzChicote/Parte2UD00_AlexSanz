def es_valida(tablero, fila, columna):
    """Comprueba si es seguro colocar una reina en la fila y columna x"""
    for i in range(fila):
        # Revisa si hay otra reina en la misma columna
        if tablero[i] == columna:
            return False
        # Revisa si hay otra reina en las diagonales
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    return True


def resolver_n_reinas(fila, tablero, n):
    ##Calcula recursivamente las soluciones posibles
    if fila == n:
        # Se han colocado todas las reinas con éxito
        return 1

    soluciones = 0
    for columna in range(n):
        if es_valida(tablero, fila, columna):
            tablero[fila] = columna
            # Continúa probando en la siguiente fila
            soluciones += resolver_n_reinas(fila + 1, tablero, n)

    return soluciones


def obtener_soluciones_totales(n):
    # Inicia el cálculo para un tamaño N
    tablero = [-1] * n
    return resolver_n_reinas(0, tablero, n)

# Prueba 
if __name__ == "__main__":
    print(f"{'Tamaño N':<10} | {'Soluciones totales':<20}")
    print("-" * 35)

    for n in range(4, 11):
        total = obtener_soluciones_totales(n)
        print(f"{n:<10} | {total:<20}")

