
import csv
import sys
from pathlib import Path
import barcode
from barcode.writer import ImageWriter




def formatear_id_ean13(id_texto: str) -> str:
   """Limpia el ID y lo ajusta a 12 dígitos para ser compatible con EAN-13."""
   id_limpio = id_texto.strip().strip('"').strip("'")


   if not id_limpio.isdigit():
       raise ValueError(
           f"El id '{id_texto}' solo puede contener números."
       )


   if len(id_limpio) < 12:
       return id_limpio.zfill(12)
   elif len(id_limpio) in (12, 13):
       return id_limpio
   else:
       raise ValueError(
           f"El id '{id_texto}' supera los 13 dígitos permitidos."
       )




def generar_codigos_alumnos(ruta_csv: str):
   path_csv = Path(ruta_csv)


   # Validar existencia del archivo
   if not path_csv.is_file():
       print(
           f"Error: No se encontró el archivo '{ruta_csv}'.", file=sys.stderr
       )
       sys.exit(1)


   # Cargar formato EAN13 para imágenes
   EAN13 = barcode.get_barcode_class("ean13")


   with open(path_csv, mode="r", encoding="utf-8") as f:
       lector = csv.reader(f)


       for num_linea, fila in enumerate(lector, start=1):
           # Ignorar líneas vacías
           if not fila:
               continue


           # Validar columnas
           if len(fila) < 2:
               print(
                   f"[Línea {num_linea}] Formato incorrecto. Debe ser 'nombre, id'."
               )
               continue


           nombre_alumno = fila[0].strip().strip('"')
           id_raw = fila[1].strip().strip('"')


           try:
               # Ajustar id a 12 dígitos
               id_valido = formatear_id_ean13(id_raw)


               # Generar código de barras en PNG
               codigo_barras = EAN13(id_valido, writer=ImageWriter())


               # Guardar imagen PNG
               nombre_archivo = nombre_alumno
               ruta_generada = codigo_barras.save(nombre_archivo)


               print(
                   f"Generado: {ruta_generada} | Alumno: {nombre_alumno} | Código: {codigo_barras.get_fullcode()}"
               )


           except Exception as e:
               print(
                   f"Error en la línea {num_linea} ({nombre_alumno}): {e}",
                   file=sys.stderr,
               )




if __name__ == "__main__":
   # Comprobar argumento CSV en consola
   if len(sys.argv) < 2:
       print("Uso del programa:")
       print("  python generar_codigos.py <archivo.csv>")
       sys.exit(1)


   archivo_argumento = sys.argv[1]
   generar_codigos_alumnos(archivo_argumento)


