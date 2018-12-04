import json, os
from datetime import datetime

from flask import Blueprint, render_template, jsonify, request

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from models.document import Document
from watson.discovery import Discovery
from config import FILESTORE_USER_DOCUMENT_TEMPLATE

pitch_blueprint = Blueprint('pitch', __name__, url_prefix='/pitch')

@pitch_blueprint.route('/<int:pitch_id>')
def get_pitch(pitch_id):
    
    try:
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:
            
            # Provide the pitch try IDs for this pitch incase it is useful to query later
            pitch_try_ids = [x.id for x in PitchTry.query.filter_by(pitch_id=pitch.id)]

            # Try to pull pitch info from database first, then try Watson services only if available
            related_concepts = pitch.related_concepts or ''
            watson_query = ''

            try:
                wat = Discovery()
                collection = wat.getUserCollection(user_id = pitch.user_id, pitch_id = pitch.id)
                # if not collection:
                #     wat.createCollection()
                
                watson_query = wat.queryCollection(collection['collection_id'])[0]

            except Exception as e:
                print(e)
                print("[!] There was an issue connecting to Watson services.")

            if watson_query:
                related_concepts = [x['key'] for x in watson_query['results'] if 'results' in watson_query]
                pitch.related_concepts = json.dumps(related_concepts)
                db.session.add(pitch)
                db.session.commit()

            docs = {doc.id:doc.name for doc in Document.query.filter_by(pitch_id=pitch_id).all()}

            watson_data = {
                'top_entities': ['a', 'b', 'c'],
                'related_concepts': related_concepts,
                'watson_query': watson_query
            }

            data = {
                'pitch': {
                    'name': pitch.name,
                    'content_analysis': watson_data,
                    'documents': docs   
                },
                'pitch_try_ids': pitch_try_ids
            }

            return jsonify(data)

        else:
            return ('Pitch does not exist.', 404)

    except Exception as e:
        print("[!] There was a critical issue while retreiving a pitch.")
        raise e


@pitch_blueprint.route('/<int:pitch_id>/new_try', methods=['POST'])
def new_pitch_try(pitch_id):
    ''' Add a new pitch try '''

    try:
        # Make sure pitch exists
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:

            # Get args and provide defaults
            inc_data = request.json
            transcription = inc_data.get('transcription', '')
            duration = inc_data.get('duration', 0)
            company = inc_data.get('company', '')
            
            # Create pitch try and analyze
            pitch_try = PitchTry(
                pitch_id = pitch.id,
                transcription = transcription,
                duration = duration,
                company = company
            )

            if pitch_try:
                db.session.add(pitch_try)
                db.session.commit()

                data = {
                    'pitch_try_id': pitch_try.id
                }

                return jsonify(data)
            else:
                return ('Pitch not created', 400)

        else:
            return ('Pitch does not exist in db', 404)

    except Exception as e:
        print("[!] There was a critical issue while creating a new pitch try.")
        raise e


@pitch_blueprint.route('/<int:pitch_id>/pitch_tries')
def get_pitch_tries_for_pitch(pitch_id):
    
    data = {
        'pitches': []
    }
    
    try:
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:
            pitch_tries = PitchTry.query.filter_by(pitch_id=pitch.id)

            if pitch_tries:
                
                for pitch_try in pitch_tries:
                    pitch_try_data = {
                        'id': pitch_try.id,
                        'duration': pitch_try.duration,
                        'timestamp': '123', # make date
                        'score': 88 # make metric
                    }

                    data['pitches'].append(pitch_try_data)

            else:
                data['msg'] = "No pitch tries for this pitch ID"

            return jsonify(data)

        else:
            return ('This pitch ID does not exist.', 404)

    except Exception as e:
        # TODO something meaningful
        raise e

@pitch_blueprint.route('/delete/<int:pitch_id>')
def delete_pitch(pitch_id):
    try:
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:
            db.session.delete(pitch)
            db.session.commit()

            return ('', 200)
        else:
            return ('This pitch try does not exist', 404)
    except Exception as e:
        return (e, 500)

@pitch_blueprint.route('/<int:pitch_id>/upload', methods=['POST'])
def upload_document(pitch_id):
    ''' Upload a document to a pitch '''

    try:

        # Make sure pitch exists
        pitch = Pitch.query.filter_by(id=pitch_id).first()

        if pitch:

            user_id = pitch.user_id

            # Using the bottom version to account for multi-file upload.
            # files = request.files.to_dict(flat=False)

            files = request.files.getlist('files[]')
            file_names = []

            for file_obj in files:
                print("Getting file:", file_obj)

                # Add file name to a list to use for Discovery
                file_names.append(file_obj.filename)
                file_obj.save(os.path.join(FILESTORE_USER_DOCUMENT_TEMPLATE.format(user_id, pitch_id), file_obj.filename))

            # Error checking for later, more or less
            # if 'file' not in request.files:
            #     print("No file uploaded")
            #     return ("No file uploaded", 400)

            # Create a Discovery instance and upload this doc for the user
            try:
                wat = Discovery()
                user_collection = wat.getUserCollection(user_id, pitch_id)

                if not user_collection:
                    user_collection = wat.createUserCollection(user_id, pitch_id)

                user_collection_id = user_collection['collection_id']

                # Upload all documents to collection and local database
                for file_name in file_names:
                    wat.addDocument(user_id, pitch_id, user_collection_id, file_name)

                    print("Adding", file_name, "to pitch:", pitch.name)
                    local_doc = Document(name = file_name, pitch_id = pitch.id)
                    if local_doc:
                        db.session.add(local_doc)
                        db.session.commit()
                        print("Added to DB!")
                        return 'Added Document'

            except Exception as e:
                print("[!] An error occurred when attempting to upload a file to Watson.")
                raise e

    except Exception as e:
        print("[!] An error occurred when attempting to upload a file.")
        raise e
        
    return ('', 200)