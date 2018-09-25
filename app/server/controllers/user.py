import os
from flask import Blueprint
from flask import request
from flask import current_app
from six.moves.urllib.parse import urlencode

from models.user import User
from models.pitch import Pitch

from database import db

from helpers.authenticate import requires_auth

user_blueprint = Blueprint('user', __name__, template_folder=None)

@user_blueprint.route('/<int:single_id>', methods=['GET'])
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

@user_blueprint.route('/', methods=['POST'])
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
            db.session.add(user)
            db.session.commit()

            return str(user.id)
        else:
            return 'user not created'
    except Exception as e:
        raise e


@user_blueprint.route('/<int:single_id>/new_pitch', methods=['POST'])
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

@user_blueprint.route('/upload', methods=['GET', 'POST'])
# @requires_auth
def upload():
    file = request.files['file']
    filename = file.filename

    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    
    return ('', 200)
