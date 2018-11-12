import os
import json
from watson_developer_cloud import ToneAnalyzerV3

class ToneAnalyzer(object):
    def __init__(self):

        print(os.getenv("TONE_ANALYZER_PASSWORD"))

        self.tone_analyzer = ToneAnalyzerV3(
            version=os.getenv("TONE_ANALYZER_VERSION"),
            url=os.getenv("TONE_ANALYZER_URL"),
            username=os.getenv("TONE_ANALYZER_USERNAME"),
            password=os.getenv("TONE_ANALYZER_PASSWORD")
        )

    def analyzeTone(self, text):
        return self.tone_analyzer.tone(
            {'text': text},
            'application/json').get_result()
