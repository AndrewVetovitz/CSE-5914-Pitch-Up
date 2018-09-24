import os
from os.path import join, dirname
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controllers.user import user_blueprint
from controllers.report import report_blueprint

# SQLITE_DB_LOCATION = 'sqlite:///db/test.db'

from controllers.watson.speech_to_text import SpeechToText
from controllers.watson.discovery import Discovery

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_LOCATION
# db = SQLAlchemy(app)

app.register_blueprint(user_blueprint)

# speechToText = SpeechToText()

# audio_file = open(join(dirname(__file__), 'audio/1/1/recording1.mp3'), 'rb')

# speechToText.translateSpeech(audio_file)

# print('finished')

# audio_file.close()

discovery = Discovery()

discovery.createCollection('0', '0', 'test', 'test collection', 'en')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
