from pymongo import MongoClient

# Configuración de la conexión
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "star_wars_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Colección de personajes
characters_collection = db["characters"]

def insert_character(character):
    """
    Inserta un personaje en la colección de MongoDB.
    :param character: Diccionario con los datos del personaje.
    """
    characters_collection.update_one(
        {"name": character["name"]},  # Evita duplicados basados en el nombre
        {"$set": character},
        upsert=True
    )

def get_all_characters():
    """
    Obtiene todos los personajes de la colección.
    :return: Lista de personajes.
    """
    return list(characters_collection.find({}, {"_id": 0}))  # Excluye el campo _id

def get_character_by_name(name):
    """
    Obtiene un personaje por su nombre.
    :param name: Nombre del personaje.
    :return: Diccionario con los datos del personaje.
    """
    return characters_collection.find_one({"name": name}, {"_id": 0})