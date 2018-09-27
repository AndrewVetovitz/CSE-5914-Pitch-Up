from datetime import datetime
import json

from flask import Blueprint, render_template, jsonify, request

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from watson.discovery import Discovery


pitch_blueprint = Blueprint('pitch', __name__, url_prefix='/pitch')


@pitch_blueprint.route('/<int:pitch_id>')
def get_pitch(pitch_id):
    
    try:
     
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:

            pitch_try_ids = [x.id for x in PitchTry.query.filter_by(pitch_id=pitch.id)]

            wat = Discovery()
            collection = wat.getUserCollection(user_id = pitch.user_id, pitch_id = pitch.id)
            watson_query = wat.queryCollection(collection['collection_id'])[0]

            if watson_query:

                # Related concepts
                related_concepts = [x['key'] for x in watson_query['results'] if 'results' in watson_query]
                pitch.related_concepts = json.dumps(related_concepts)
                db.session.add(pitch)
                db.session.commit()
                            

            # TODO Do same thing for top entities
            watson_data = {
                'top_entities': ['a', 'b', 'c'],
                'related_concepts': related_concepts,
                'watson_query': watson_query
            }

            data = {
                'pitch': {
                    'name': pitch.name,
                    'content_analysis': watson_data                
                },
                'pitch_try_ids': pitch_try_ids
            }

            return jsonify(data)

        else:

            return ('', 404)

    except Exception as e:
        # TODO something meaningful
        raise e


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
            transcription = inc_data.get('transcription', '')
            duration = inc_data.get('pitch_duration', 0)

            # debug
            print(inc_data)
            
            # Create pitch try and analyze
            pitch_try = PitchTry(
                pitch_id = pitch.id,
                transcription = transcription,
                duration = duration
            )
            

            if pitch_try:

                pitch_try.analyze()

                db.session.add(pitch_try)
                db.session.commit()
                
                # debug
                print(pitch_try)

                data = {
                    'pitch_try_id': pitch_try.id
                }

                return jsonify(data)

            else:
                return 'pitch not created'

        else:
            return 'pitch does not exist in db'

    except Exception as e:
        raise e

