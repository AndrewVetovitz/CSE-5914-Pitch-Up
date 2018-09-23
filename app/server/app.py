import os
from os.path import join, dirname
from flask import Flask

from controllers.user import user_blueprint

from controllers.watson.speech_to_text import SpeechToText

app = Flask(__name__)

app.register_blueprint(user_blueprint)

speechToText = SpeechToText()

audio_file = open(join(dirname(__file__), 'audio/1/1/recording1.mp3'), 'rb')

speechToText.translateSpeech(audio_file)

print('finished')

audio_file.close()
