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
    
    try:
        pitch_try = PitchTry.query.filter_by(id=pitch_try_id).first()

        if pitch_try:
            print(pitch_try)

            data = {
                'pitch_try': {
                    'id': pitch_try.id,
                    'is_analyzed': pitch_try.is_analyzed,
                    'transcription': pitch_try.transcription,
                    'analysis_words': json.loads(pitch_try.analysis_words),
                    'analysis_concepts': pitch_try.analysis_concepts,
                    'duration': pitch_try.duration,
                    'words_per_minute': pitch_try.words_per_minute
                    # TODO need date still, but needs special json parsing usually.
                }
            }

            return jsonify(data)
        else:
            return ('', 404)
    except Exception as e:
        # TODO something meaningful
        raise e
