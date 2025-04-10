import requests

def get_request(url):
    """
    This function sends a GET request to the specified URL and returns the response.
    :param url: The URL to send the GET request to.
    :return: The response from the server.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def guardar_json(response, filename):
    """
    This function saves the JSON content of the response to a file.
    :param response: The response object from the GET request.
    :param filename: The name of the file to save the JSON content to.
    """
    try:
        with open(filename, 'w') as f:
            f.write(response.text)
        print(f"JSON content saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

#puerto de la base de datos = 5432