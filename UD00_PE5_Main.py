# Crear la escuela inicial
escuela = Escuela("IES Fasuti Barbera", "Alaquas", "Fausti Barbera")


opcion = ""


while opcion != "0":
   print("\n Gestion Escuela ")
   print("1. Añadir profesor")
   print("2. Modificar profesor")
   print("3. Eliminar profesor")
   print("4. Añadir alumno")
   print("5. Modificar alumno")
   print("6. Eliminar alumno")
   print("7. Mostrar todo")
   print("0. Salir")
  
   opcion = input("Elige una opción: ")


   if opcion == "1":
       dni = input("DNI: ")
       nombre = input("Nombre: ")
       tipo = input("Tipo (ciencias/letras/mixto): ")
       escuela.anadir_profesor(dni, nombre, tipo)


   elif opcion == "2":
       dni = input("DNI del profesor a modificar: ")
       nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
       tipo = input("Nuevo tipo (deja en blanco para no cambiar): ")
       escuela.modificar_profesor(dni, nombre, tipo)


   elif opcion == "3":
       dni = input("DNI del profesor a eliminar: ")
       escuela.eliminar_profesor(dni)


   elif opcion == "4":
       id_a = input("ID alumno: ")
       nombre = input("Nombre: ")
       curso = input("Curso: ")
       dni_p = input("DNI del profesor asignado (opcional): ")
       escuela.anadir_alumno(id_a, nombre, curso, dni_p)


   elif opcion == "5":
       id_a = input("ID del alumno a modificar: ")
       nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
       curso = input("Nuevo curso (deja en blanco para no cambiar): ")
       dni_p = input("Nuevo DNI de profesor (deja en blanco para no cambiar): ")
       escuela.modificar_alumno(id_a, nombre, curso, dni_p)


   elif opcion == "6":
       id_a = input("ID del alumno a eliminar: ")
       escuela.eliminar_alumno(id_a)


   elif opcion == "7":
       escuela.mostrar_todo()


   elif opcion == "0":
       print("Saliendo del programa...")
   else:
       print("Opción no válida.")


