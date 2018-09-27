import os
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource

class DataCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))
        return data

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


class SpeechToText(object):
    def __init__(self):
        self.speech_to_text = SpeechToTextV1(
            username=os.getenv("SPEECH_TO_TEXT_USERNAME"),
            password=os.getenv("SPEECH_TO_TEXT_PASSWORD"),
            url=os.getenv("SPEECH_TO_TEXT_URL")
        )

    def translateSpeech(self, audio_file):
        audio_type = 'audio/mp3'
        audio_source = AudioSource(audio_file)
        dataCallback = DataCallback()

        self.speech_to_text.recognize_using_websocket(
            audio=audio_source,
            content_type=audio_type,
            recognize_callback=dataCallback,
            model='en-US_BroadbandModel')
