import requests

# Pedimos la especie al usuario por teclado
especie = input("Introduce la especie de los personajes (Human, Alien...): ")

# URL de la API de Rick and Morty filtrando por especie
url = f"https://rickandmortyapi.com/api/character/?species={especie}"

# Hacemos la petición a la API
respuesta = requests.get(url)

# Comprobamos si la respuesta es correcta (código 200)
if respuesta.status_code == 200:
    # Convertimos la respuesta que viene de la api a formato json como a un diccionario
    datos = respuesta.json()
    
    # Extraemos la lista de personajes
    personajes = datos.get("results", [])
    
    print(f"\nPersonajes encontrados de la especie '{especie}' ")
    # Recorremos cada personaje y mostramos su nombre y estado
    for personaje in personajes:
        print(f"- {personaje['name']} (Estado: {personaje['status']})")

elif respuesta.status_code == 404:
    print(f"\nNo se han encontrado personajes para la especie '{especie}'.")
else:
    print("\nHa ocurrido un error al conectar con la API.")