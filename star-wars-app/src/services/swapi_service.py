from utils.prueba_request import get_request

def fetch_characters():
    """
    Fetches the list of characters from the SWAPI.
    :return: A list of characters or None if an error occurs.
    """
    url = "https://swapi.dev/api/people/"
    response = get_request(url)
    if response:
        return response.json().get('results', [])
    return None

def fetch_character_details(character_url):
    """
    Fetches details for a specific character from the SWAPI.
    :param character_url: The URL of the character to fetch details for.
    :return: A dictionary containing character details or None if an error occurs.
    """
    response = get_request(character_url)
    if response:
        return response.json()
    return None