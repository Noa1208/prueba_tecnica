from flask import Blueprint, render_template

detail_screen = Blueprint('detail_screen', __name__)

@detail_screen.route('/character/<int:character_id>')
def character_detail(character_id):
    # Aquí normalmente se obtienen los detalles del personaje usando character_id
    # Por ahora, usaremos datos de marcador de posición
    character = {
        'name': 'Luke Skywalker',
        'height': '172',
        'weight': '77',
        'gender': 'male',
        'films': [
            'A New Hope',
            'The Empire Strikes Back',
            'Return of the Jedi'
        ]
    }
    
    return render_template('detail_screen.html', character=character)