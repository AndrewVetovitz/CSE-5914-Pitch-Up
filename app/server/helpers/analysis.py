import json

class Analysis(object):
    def words_per_minute(self, transcript, duration):
        if duration == 0:
            return 0
        else:
            trans_list = transcript.split()
            
            words_per_minute = float(len(trans_list) * 60) / float(duration)
            return round(words_per_minute, 2)

    def num_occurences(self, transcript, word_list):
        trans_list = transcript.split()
        count = 0
        
        for word in word_list:
            if word in trans_list:
                count += 1

        return count

    def discovery_analysis(self, transcript, pitch):
        analysis_concepts = ''
        trans_list = transcript.split()
        concept_analysis = {}

        if pitch.related_concepts:
            concepts = (" ".join(json.loads(pitch.related_concepts)).lower()).split()
            for word in trans_list:
                if word in concepts:
                    concept_analysis[word] = concept_analysis.get(word, 0) + 1
            
            analysis_concepts = json.dumps(concept_analysis)

        return analysis_concepts
