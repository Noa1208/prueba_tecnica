from flask import Flask, render_template, redirect, url_for
import requests
from services.swapi_service import fetch_characters

app = Flask(__name__)

@app.route('/')
def main_screen():
    characters = fetch_characters()
    return render_template('main_screen.html', characters=characters)

@app.route('/character/<int:character_id>')
def detail_screen(character_id):
    character = fetch_character_details(character_id)
    return render_template('detail_screen.html', character=character)

if __name__ == '__main__':
    app.run(debug=True)