from datetime import datetime
import json

from flask import Blueprint, render_template, jsonify, request

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from watson.discovery import Discovery

pitch_try_blueprint = Blueprint('pitch_try', __name__, url_prefix='/pitch_try')

@pitch_try_blueprint.route('/<int:pitch_try_id>')
def get_pitch_try(pitch_try_id):
    ''' Return a single user by id if they exist '''

    try:
        pitch_try = PitchTry.query.filter_by(id=pitch_try_id).first()

        if pitch_try and pitch_try.is_analyzed:
            return jsonify(pitch_try.serialize)
        else:
            return ('', 404)
    except Exception as e:
        raise e

@pitch_try_blueprint.route('/delete/<int:pitch_id>/<int:pitch_try_id>')
def delete_pitch_try(pitch_id, pitch_try_id):
    ''' Delete pitch try '''
    try:
        pitch_try = PitchTry.query.filter_by(pitch_id=pitch_id).filter_by(id=pitch_try_id).first()

        if pitch_try:
            db.session.delete(pitch_try)
            db.session.commit()

            return ('', 200)
        else:
            return ('This pitch try does not exist', 404)
    except Exception as e:
        return (e, 500)
