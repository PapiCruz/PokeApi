import requests
import json
import numpy as np
import numpy
import matplotlib.pyplot as plt
import openpyxl

def bus_pokemon():
    nombre_o_id = input("\nIngrese el nombre o ID del Pokemon que desea buscar en la Pokedex: ")

    if nombre_o_id.isnumeric():
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id}"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id.lower()}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nNombre: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print(f"Altura: {data['height']/10} metros")
        print(f"Peso: {data['weight']/10} kg")
        tipos = [tipo['type']['name'] for tipo in data['types']]
        print(f"Tipos: {', '.join(tipos)}")
        guardar = input("¿Quieres guardar esta información en una pokedex de texto? (s/n): ")
        if guardar.lower() == "s":
            guardar_en_archivo(data)
        datos= input("¿Quieres guardar la altura para obtener sacar sus estadísticas? (s/n): ")
        if datos.lower() == "s":
            graficar_datos(data)
    else:
        print("\nNo se pudo encontrar el Pokemon en la Pokedex. Intente nuevamente.")


def lista_pokemon():
    offset = 0
    limit = input("Ingrese la cantidad de pokemones en lista que desea ver: ")

    if limit.isnumeric():

        while True:
            limit = int(limit)
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}")

            if response.status_code == 200:
                data = response.json()
                resultados = data['results']

                for pokemon in resultados:
                    print(pokemon['name'].capitalize())

                print("")

                while True:
                    opcion = input(f"Presione 'n' para ver los siguientes {limit} pokemones o cualquier otra tecla para volver al menú: ")

                    if opcion.lower() == 'n':
                        offset += limit
                        break
                    else:
                        return
            else:
                print("\nNo se pudieron obtener los datos. Intente nuevamente.")
                return
    else:
        print("Digito incorrecto, ingrese por favor un número")
        return
