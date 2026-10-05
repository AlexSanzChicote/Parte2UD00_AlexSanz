class Profesor:
   # Atributos del profesor
   def __init__(self, dni, nombre, tipo):
       self.dni = dni
       self.nombre = nombre
       self.tipo = tipo




class Alumno:
   # Atributos del alumno y asigna un profesor responsable opcional
   def __init__(self, id_alumno, nombre, curso, profesor_responsable=None):
       self.id_alumno = id_alumno
       self.nombre = nombre
       self.curso = curso
       self.profesor_responsable = profesor_responsable




class Escuela:
   # Datos de la escuela y las listas de profesores y alumnos
   def __init__(self, nombre, localidad, responsable):
       self.nombre = nombre
       self.localidad = localidad
       self.responsable = responsable
       self.profesores = []
       self.alumnos = []


   # Profesores


   # Crea y añade un nuevo profesor a la lista
   def anadir_profesor(self, dni, nombre, tipo):
       prof_nuevo = Profesor(dni, nombre, tipo)
       self.profesores.append(prof_nuevo)
       print("Profesor añadido correctamente.")


   # Busca y devuelve un profesor por su dni
   def buscar_profesor(self, dni):
       for prof_actual in self.profesores:
           if prof_actual.dni == dni:
               return prof_actual
       return None


   # Modifica los datos de un profesor existente
   def modificar_profesor(self, dni, nuevo_nombre, nuevo_tipo):
       prof_encontrado = self.buscar_profesor(dni)
       if prof_encontrado:
           if nuevo_nombre:
               prof_encontrado.nombre = nuevo_nombre
           if nuevo_tipo:
               prof_encontrado.tipo = nuevo_tipo
           print("Profesor modificado.")
       else:
           print("Profesor no encontrado.")


   # Elimina un profesor y desasigna sus alumnos tutorizados
   def eliminar_profesor(self, dni):
       prof_encontrado = self.buscar_profesor(dni)
       if prof_encontrado:
           for alumno_actual in self.alumnos:
               if alumno_actual.profesor_responsable == prof_encontrado:
                   alumno_actual.profesor_responsable = None
           self.profesores.remove(prof_encontrado)
           print("Profesor eliminado.")
       else:
           print("Profesor no encontrado.")


   # Alumnos


   # Crea y añade un nuevo alumno asignándole un profesor tutor si se indica
   def anadir_alumno(self, id_alumno, nombre, curso, dni_profesor=None):
       prof_tutor = self.buscar_profesor(dni_profesor) if dni_profesor else None
       alumno_nuevo = Alumno(id_alumno, nombre, curso, prof_tutor)
       self.alumnos.append(alumno_nuevo)
       print("Alumno añadido correctamente.")


   # Busca y devuelve un alumno por su id
   def buscar_alumno(self, id_alumno):
       for alumno_actual in self.alumnos:
           if alumno_actual.id_alumno == id_alumno:
               return alumno_actual
       return None


   # Modifica los datos de un alumno existente
   def modificar_alumno(self, id_alumno, nuevo_nombre, nuevo_curso, nuevo_dni_prof):
       alumno_encontrado = self.buscar_alumno(id_alumno)
       if alumno_encontrado:
           if nuevo_nombre:
               alumno_encontrado.nombre = nuevo_nombre
           if nuevo_curso:
               alumno_encontrado.curso = nuevo_curso
           if nuevo_dni_prof:
               alumno_encontrado.profesor_responsable = self.buscar_profesor(nuevo_dni_prof)
           print("Alumno modificado.")
       else:
           print("Alumno no encontrado.")


   # Elimina un alumno de la lista
   def eliminar_alumno(self, id_alumno):
       alumno_encontrado = self.buscar_alumno(id_alumno)
       if alumno_encontrado:
           self.alumnos.remove(alumno_encontrado)
           print("Alumno eliminado.")
       else:
           print("Alumno no encontrado.")






   # Muestra por pantalla toda la información de la escuela, profesores y alumnos
   def mostrar_todo(self):
       print(f"\n Escuela: {self.nombre} ({self.localidad}) | Resp: {self.responsable} ---")
      
       print("Profesorres:")
       if not self.profesores:
           print("  (Ninguno)")
       for prof_item in self.profesores:
           print(f"  - DNI: {prof_item.dni} | Nombre: {prof_item.nombre} | Tipo: {prof_item.tipo}")


       print("Alumnos:")
       if not self.alumnos:
           print("  (Ninguno)")
       for alum_item in self.alumnos:
           nombre_tutor = alum_item.profesor_responsable.nombre if alum_item.profesor_responsable else "Sin tutor"
           print(f"  - ID: {alum_item.id_alumno} | Nombre: {alum_item.nombre} | Curso: {alum_item.curso} | Tutor: {nombre_tutor}")


