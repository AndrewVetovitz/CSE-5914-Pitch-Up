import os
import json
from watson_developer_cloud import DiscoveryV1

class Discovery(object):
    def __init__(self):
        self.discovery = DiscoveryV1(
            version=os.getenv("DISCOVERY_VERSION"),
            url=os.getenv("DISCOVERY_URL"),
            username=os.getenv("DISCOVERY_USERNAME"),
            password=os.getenv("DISCOVERY_PASSWORD")
        )

    def createCollection(self, environment_id, configuration_id, collection_name, collection_desc, collection_lang):
        new_collection = self.discovery.create_collection(
            environment_id=environment_id, 
            configuration_id=configuration_id, 
            name=collection_name, 
            description=collection_desc, 
            language=collection_lang).get_result()
            
        print(json.dumps(new_collection, indent=2))
