from flask import Flask, render_template
from services.swapi_service import fetch_characters, fetch_character_details

app = Flask(__name__, template_folder='templates')

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