import os

from flask import Blueprint, request, current_app, jsonify
from six.moves.urllib.parse import urlencode
from watson.discovery import Discovery

from models.user import User
from models.pitch import Pitch
from database import db
from helpers.authenticate import requires_auth

from config import FILESTORE_USER_DOCUMENT_TEMPLATE


user_blueprint = Blueprint('user', __name__, template_folder=None, url_prefix='/user')

@user_blueprint.route('/<int:single_id>', methods=['GET'])
def single(single_id):
    ''' Returns a single user by id given they exist '''

    try:
        user = User.query.filter_by(id=single_id).first()

        if user:
            return jsonify(user.serialize)
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
        username = inc_data.get('username', '')
        email = inc_data.get('email', '')
        password = inc_data.get('password', '')
        company = inc_data.get('company', '')
        city = inc_data.get('city', '')
        state = inc_data.get('state', '')
        country = inc_data.get('country', '')
        postal = inc_data.get('postal', '')
        bio = inc_data.get('bio', '')

        user = User(name=name, username=username, email=email, password=password, company=company, city=city, state=state, country = country, postal=postal, bio=bio)

        if user:
            db.session.add(user)
            db.session.commit()

            return str(user.id)
        else:
            return 'user not created'
    except Exception as e:
        raise e

@user_blueprint.route('/update', methods=['PUT'])
def update_single():
    ''' Update a single user given an id '''

    try:
        # Get args and provide defaults
        inc_data = request.json

        id = inc_data.get('id', '')

        user = User.query.filter_by(id=id).first()

        name = inc_data.get('name', '')
        username = inc_data.get('username', '')
        email = inc_data.get('email', '')
        password = inc_data.get('password', '')
        company = inc_data.get('company', '')
        city = inc_data.get('city', '')
        state = inc_data.get('state', '')
        country = inc_data.get('country', '')
        postal = inc_data.get('postal', '')
        bio = inc_data.get('bio', '')

        user.update(name=name, username=username, email=email, password=password, company=company, city=city, state=state, country = country, postal=postal, bio=bio)

        if user:
            db.session.add(user)
            db.session.commit()

            return ('ok', 200)
        else:
            return 'user not created'
    except Exception as e:
        raise e


@user_blueprint.route('/<int:single_id>/new_pitch', methods=['POST'])
def add_pitch(single_id):
    ''' Add a pitch to a user and return the newly created pitch id '''

    try:
        # Make sure user exists
        user = User.query.filter_by(id=single_id).first()

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
                
                pitch_dir = os.path.join(FILESTORE_USER_DOCUMENT_TEMPLATE.format(user.id, pitch.id))
                # Add directory for file upload
                if not os.path.isdir(pitch_dir):
                    os.mkdir(pitch_dir)

                # debug
                print(pitch)

                return str(pitch.id)

            else:
                return 'pitch not created'
        else:
            return 'user does not exist in db'
    except Exception as e:
        raise e


@user_blueprint.route('/<int:single_id>/pitches', methods=['GET'])
def get_user_pitches(single_id):
    ''' Get all pitches associated with a user ID '''

    data = {
        'pitches': []
    }

    try:
        # Make sure user exists
        user = User.query.filter_by(id=single_id).first()

        if user:
            pitches = Pitch.query.filter_by(user_id=user.id).all()

            # Add pitches that we found, otherwise, the return will be the
            # empty list
            if pitches:
                
                for pitch in pitches:
                    pitch_data = {
                        'id': pitch.id,
                        'name': pitch.name,

                    }

                    data['pitches'].append(pitch_data)

                return jsonify(data)

            else:
                return ('No pitches available for this user ID', 404)
        else:
            return ('User does not exist in db', 404)

    except Exception as e:
        raise e
