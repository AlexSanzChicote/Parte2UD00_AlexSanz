import shutil
from pathlib import Path




def organizar_archivos(extensiones: list[str]):
   # Directorio de ejecución
   directorio_actual = Path.cwd()


   for ext in extensiones:
       # Limpiar extensión (quitar punto inicial)
       ext_clean = ext.strip().lstrip(".")


       if not ext_clean:
           continue


       # Carpeta destino
       carpeta_destino = directorio_actual / ext_clean


       # Buscar archivos
       pattern = f"*.{ext_clean}"
       archivos = [
           f
           for f in directorio_actual.glob(pattern)
           if f.is_file() and f.suffix.lower() == f".{ext_clean.lower()}"
       ]


       if archivos:
           # Crear carpeta destino
           carpeta_destino.mkdir(exist_ok=True)


           for archivo in archivos:
               destino_archivo = carpeta_destino / archivo.name
               try:
                   shutil.move(str(archivo), str(destino_archivo))
                   print(
                       f"Movido: {archivo.name} -> {ext_clean}/{archivo.name}"
                   )
               except Exception as e:
                   print(
                       f"Error al mover {archivo.name}: {e}"
                   )




if __name__ == "__main__":
   # Extensiones a organizar
   lista_extensiones = ["png", "mp4", "doc", "pdf", "txt"]


   print("Iniciando la organización de archivos...")
   organizar_archivos(lista_extensiones)
   print("¡Proceso finalizado con éxito!")

