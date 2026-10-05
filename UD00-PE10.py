import sys
from pathlib import Path
from PIL import Image
from pyzbar.pyzbar import decode




def leer_codigos_directorio(directorio: str = "."):
   ruta_dir = Path(directorio)


   # Validar existencia del directorio
   if not ruta_dir.is_dir():
       print(
           f"Error: El directorio '{directorio}' no existe.", file=sys.stderr
       )
       sys.exit(1)


   # Obtener archivos .png
   archivos_png = sorted(list(ruta_dir.glob("*.png")))


   if not archivos_png:
       print(f"No se encontraron archivos .png en '{ruta_dir}'.")
       return


   print(f"Se encontraron {len(archivos_png)} archivos png.\n")
   print(f"{'Nombre Alumno':<25} | {'ID del alumno'}")
   print("-" * 50)


   for archivo in archivos_png:
       # Nombre del alumno desde el archivo
       nombre_alumno = archivo.stem


       try:
           # Abrir imagen
           imagen = Image.open(archivo)


           # Leer códigos de barras
           codigos_detectados = decode(imagen)


           if not codigos_detectados:
               print(
                   f"{nombre_alumno:<25} | [No se detectó ningún código de barras]"
               )
               continue


           for codigo in codigos_detectados:
               # Extraer texto del código
               dato_raw = codigo.data.decode("utf-8")


               # Limpiar ceros a la izquierda y quitar el dígito final (es de control)
               id_limpio = dato_raw.lstrip("0")
               if len(id_limpio) > 1:
                   id_limpio = id_limpio[:-1]


               print(f"{nombre_alumno:<25} | {id_limpio}")


       except Exception as e:
           print(f"{nombre_alumno:<25} | Error al leer el archivo: {e}")




if __name__ == "__main__":
   # Usar ruta enviada por consola o el directorio actual
   dir_input = sys.argv[1] if len(sys.argv) > 1 else "."
   leer_codigos_directorio(dir_input)
