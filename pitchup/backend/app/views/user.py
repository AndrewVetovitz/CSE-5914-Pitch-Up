from flask import Blueprint, render_template, jsonify, request

from app.database import db
from app.models import User, Pitch, PitchTry


mod = Blueprint('user', __name__, url_prefix='/user')




@mod.route('/<int:single_id>', methods=['GET'])
def single(single_id):
    ''' Get a single user given an id '''

    try:
        user = User.query.filter_by(id=single_id).first()

        if user:

            return "ID: {}, Name: {}".format(str(user.id), user.name)

        else:

            return 'user not found'
    
    except Exception as e:
        raise e


@mod.route('/', methods=['POST'])
def add_single():
    ''' Add a user and return the newly created user ID on success '''

    try:

        # Get args and provide defaults
        inc_data = request.json
        name = inc_data.get('name', '')
        email = inc_data.get('email', '')
        password = inc_data.get('password', '')

        #debug
        print(inc_data)

        user = User(name=name, email=email, password=password)

        if user:

            return str(user.id)

        else:

            return 'user not created'
    
    except Exception as e:
        raise e


@mod.route('/<int:single_id>/new_pitch', methods=['POST'])
def add_pitch(single_id):
    ''' Add a pitch to a user and return the newly created pitch id '''

    try:

        # Make sure user exists
        user = User.query.filter_by(id=single_id)

        if user:

            # Get args and provide defaults
            inc_data = request.json
            pitch_name = inc_data.get('name', '')

            # debug
            print(inc_data)

            pitch = Pitch(user_id=single_id, name=pitch_name)

            if pitch:

                db.session.add(pitch)
                db.session.commit()
                
                # debug
                print(pitch)

                return str(pitch.id)

            else:

                return 'pitch not created'
        
        else:

            return 'user does not exist in db'
    
    except Exception as e:
        raise e