import os
import json
from watson_developer_cloud import ToneAnalyzerV3

class ToneAnalyzer(object):
    def __init__(self):
        self.tone_analyzer = ToneAnalyzerV3(
            version=os.getenv("TONE_ANALYZER_VERSION"),
            url=os.getenv("TONE_ANALYZER_URL"),
            username=os.getenv("TONE_ANALYZER_USERNAME"),
            password=os.getenv("TONE_ANALYZER_PASSWORD")
        )

    def analyzeTone(self, text):
        tone_analysis = self.tone_analyzer.tone(
            {'text': text},
            'application/json').get_result()
            
        print(json.dumps(tone_analysis, indent=2))
