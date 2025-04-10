from flask import Blueprint, render_template

detail_screen = Blueprint('detail_screen', __name__)

@detail_screen.route('/character/<int:character_id>')
def character_detail(character_id):
    # Here you would typically fetch the character details using the character_id
    # For now, we will use placeholder data
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