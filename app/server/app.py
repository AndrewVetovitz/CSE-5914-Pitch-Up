import os
from os.path import join
from os.path import dirname
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode

from controllers.user import user_blueprint
from controllers.report import report_blueprint

from controllers.watson.speech_to_text import SpeechToText
from controllers.watson.discovery import Discovery
from controllers.watson.tone_analyzer import ToneAnalyzer

from helpers.authenticate import AuthError

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER")

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# SQLITE_DB_LOCATION = 'sqlite:///db/test.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_LOCATION
# db = SQLAlchemy(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(report_blueprint)

def test():
    '''TEST CODE START'''
    # speechToText = SpeechToText()

    # audio_file = open(join(dirname(__file__), 'audio/1/1/recording1.mp3'), 'rb')

    # speechToText.translateSpeech(audio_file)

    # print('finished')

    # audio_file.close()

    # discovery = Discovery()

    # discovery.createCollection('0', '0', 'test', 'test collection', 'en')

    # tone = ToneAnalyzer()

    # tone.analyzeTone('Hi my name is Andrew. I love life a lot. Life is great!')
    # '''TEST CODE END'''

test()

if __name__ == "__main__":
    app.run(debug=True, port=5000)