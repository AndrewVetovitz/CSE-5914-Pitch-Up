from datetime import datetime

from flask import Blueprint, render_template, jsonify, request

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from helpers.analysis import analyze_pitch_try


pitch_blueprint = Blueprint('pitch', __name__, url_prefix='/pitch')


@pitch_blueprint.route('/')
def index():
    return 'Pitch'


@pitch_blueprint.route('/<int:pitch_id>/new_try', methods=['POST'])
def new_pitch_try(pitch_id):
    ''' Add a new pitch try '''

    try:

        # Make sure pitch user exists
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:

            print("Pitch:", pitch)

            # Get args and provide defaults
            inc_data = request.json
            timestamp = datetime.now()
            transcription = inc_data.get('transcription', '')
            duration = inc_data.get('pitch_duration', 0)

            # debug
            print(inc_data)
            
            # Create pitch try and analyze
            pitch_try = PitchTry(
                pitch_id = pitch.id,
                date = timestamp,
                transcription = transcription,
                duration = duration
            )
            

            if pitch_try:

                pitch_try.analyze()

                db.session.add(pitch_try)
                db.session.commit()
                
                # debug
                print(pitch_try)

                return str(pitch_try.id)

            else:
                return 'pitch not created'

        else:
            return 'pitch does not exist in db'

    except Exception as e:
        raise e
