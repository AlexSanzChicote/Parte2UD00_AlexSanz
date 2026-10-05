import sys
import time
import re
import pyperclip

# Lee el archivo de texto y devuelve una lista con las palabras prohibidas
def cargar_palabras_prohibidas(fichero):
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            # Leemos cada línea, quita espacios sobrantes y elimina líneas vacías
            return [linea.strip() for linea in f if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{fichero}'.")
        sys.exit(1)

# Sustituye las palabras prohibidas del texto por asteriscos
def censurar_texto(texto, palabras_prohibidas):
    texto_censurado = texto
    for palabra in palabras_prohibidas:
        # Buscamos la palabra exacta sin diferenciar mayúsculas y minúsculas
        patron = re.compile(rf'\b{re.escape(palabra)}\b', re.IGNORECASE)
        # Reemplaza la palabra por asteriscos según su longitud
        texto_censurado = patron.sub('*' * len(palabra), texto_censurado)
    return texto_censurado

def main():
    # Comprueba que se pase el archivo por parámetro en la consola
    if len(sys.argv) < 2:
        print("Uso: python programa.py <archivo_de_palabras.txt>")
        sys.exit(1)

    fichero_palabras = sys.argv[1]
    palabras_prohibidas = cargar_palabras_prohibidas(fichero_palabras)

    print(f"Programa iniciado. Vigilando el portapapeles...")
    print("Presiona Ctrl+C para salir.")

    # Guarda el último texto copiado para no repetirlo 
    ultimo_texto = ""

    try:
        while True:
            # Obtiene el texto actual del portapapeles
            texto_actual = pyperclip.paste()

            # Si el texto ha cambiado y no está vacío
            if texto_actual != ultimo_texto and texto_actual:
                texto_censurado = censurar_texto(texto_actual, palabras_prohibidas)

                # Si se detecta palabras prohibidas, actualiza el portapapeles
                if texto_censurado != texto_actual:
                    pyperclip.copy(texto_censurado)
                    print("\nTexto censurado detectado:")
                    print(f"Original:  {texto_actual}")
                    print(f"Censurado: {texto_censurado}")
                    ultimo_texto = texto_censurado
                else:
                    ultimo_texto = texto_actual

            # Espera medio segundo antes de volver a revisar
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nPrograma detenido.")

if __name__ == "__main__":
    main()

