

import csv
import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput




# Clase para organizar la pantalla de login
class VentanaLogin(BoxLayout):


   def __init__(self, **kwargs):
       super().__init__(**kwargs)


       # Ponemos los elementos uno debajo de otro
       self.orientation = "vertical"
       self.padding = 20
       self.spacing = 10


       # Guardaremos aquí los usuarios y sus contraseñas
       self.usuarios = {}


       # Leemos el archivo CSV al arrancar el programa
       self.cargar_usuarios_csv()


       # Texto y caja para escribir el usuario
       self.add_widget(Label(text="Usuario:"))
       self.input_usuario = TextInput(multiline=False)
       self.add_widget(self.input_usuario)


       # Texto y caja para la contraseña (oculta al escribir)
       self.add_widget(Label(text="Contraseña:"))
       self.input_password = TextInput(multiline=False, password=True)
       self.add_widget(self.input_password)


       # Botón que llama a la función de comprobar cuando lo pulsas
       self.boton_comprobar = Button(text="Comprobar")
       self.boton_comprobar.bind(on_press=self.comprobar_login)
       self.add_widget(self.boton_comprobar)


       # Texto final donde saldrá OK o ERROR
       self.label_resultado = Label(text="", font_size="20sp")
       self.add_widget(self.label_resultado)


   def cargar_usuarios_csv(self):
       """Lee el fichero users.csv y guarda los datos en memoria"""
       try:
           with open("users.csv", mode="r", encoding="utf-8") as archivo:
               lineas = csv.reader(archivo, delimiter=":")
               for fila in lineas:
                   if len(fila) == 2:
                       usuario = fila[0].strip().replace('"', "")
                       hash_sha1 = fila[1].strip().replace('"', "")
                       self.usuarios[usuario] = hash_sha1
       except FileNotFoundError:
           print("No se ha encontrado el archivo users.csv")


   def calcular_sha1(self, texto):
       """Encripta un texto en formato SHA1"""
       hash_objeto = hashlib.sha1(texto.encode("utf-8"))
       return hash_objeto.hexdigest()


   def comprobar_login(self, instance):
       """Revisa si el usuario existe y si la clave encriptada coincide"""
       usuario_ingresado = self.input_usuario.text.strip()
       password_ingresada = self.input_password.text.strip()


       # Encriptamos la clave introducida
       password_sha1 = self.calcular_sha1(password_ingresada)


       # Comprobamos si el usuario existe y la clave es correcta
       if (
           usuario_ingresado in self.usuarios
           and self.usuarios[usuario_ingresado] == password_sha1
       ):
           self.label_resultado.text = "OK"
           self.label_resultado.color = (0, 1, 0, 1)  # Texto en verde
       else:
           self.label_resultado.text = "ERROR"
           self.label_resultado.color = (1, 0, 0, 1)  # Texto en rojo




# Clase principal de Kivy para lanzar la app
class AplicacionLogin(App):


   def build(self):
       self.title = "Control de Acceso"
       return VentanaLogin()




if __name__ == "__main__":
   AplicacionLogin().run()


