from flask import Flask, render_template
from services.database import get_all_characters, get_character_by_name

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main_screen():
    characters = get_all_characters()
    return render_template('main_screen.html', characters=characters)

@app.route('/character/<name>')
def detail_screen(name):
    character = get_character_by_name(name)
    if not character:
        return "Personaje no encontrado.", 404
    return render_template('detail_screen.html', character=character)

if __name__ == '__main__':
    app.run(debug=True)