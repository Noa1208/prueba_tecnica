from utils.prueba_request import get_request
from services.database import insert_character

BASE_URL = "https://swapi.dev/api/people/"

def fetch_and_store_characters():
    """
    Obtiene todos los personajes de la API de SWAPI y los guarda en MongoDB.
    """
    url = BASE_URL
    while url:
        response = get_request(url)
        if response:
            data = response.json()
            for character in data['results']:
                # Obtener los títulos de las películas
                film_titles = []
                for film_url in character.get("films", []):
                    film_response = get_request(film_url)
                    if (film_response):
                        film_data = film_response.json()
                        film_titles.append(film_data.get("title", "Desconocido"))
                    else:
                        film_titles.append("Desconocido")

                # Reemplazar las URLs de las películas con sus títulos
                character["films"] = film_titles

                # Guardar el personaje en MongoDB
                insert_character(character)

            url = data.get('next')  # Ir a la siguiente página si existe
        else:
            print("Error al obtener los personajes.")
            break

def fetch_character_details(character_url):
    """
    Fetches details for a specific character from the SWAPI, including film titles.
    :param character_url: The URL of the character to fetch details for.
    :return: A dictionary containing character details or None if an error occurs.
    """
    response = get_request(character_url)
    if response:
        character = response.json()

        # Obtener los títulos de las películas
        film_titles = []
        for film_url in character.get("films", []):
            film_response = get_request(film_url)
            if film_response:
                film_data = film_response.json()
                film_titles.append(film_data.get("title", "Desconocido"))
            else:
                film_titles.append("Desconocido")

        # Reemplazar las URLs de las películas con sus títulos
        character["films"] = film_titles
        return character
    return None