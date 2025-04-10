from utils.prueba_request import get_request

def fetch_characters():
    """
    Fetches the complete list of characters from the SWAPI by iterating through all pages.
    :return: A list of all characters or None if an error occurs.
    """
    url = "https://swapi.dev/api/people/"
    all_characters = []

    while url:
        response = get_request(url)
        if response:
            data = response.json()
            all_characters.extend(data.get('results', []))  # Add characters from the current page
            url = data.get('next')  # Get the URL for the next page
        else:
            print("Error fetching data from SWAPI.")
            break

    return all_characters

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