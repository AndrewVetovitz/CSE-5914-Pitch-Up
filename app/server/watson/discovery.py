import os
import json
from watson_developer_cloud import DiscoveryV1

from config import APP_ROOT, FILESTORE_PATH, FILESTORE_USER_DOCUMENT_ROOT, FILESTORE_USER_DOCUMENT_TEMPLATE

PITCHUP_DISCOVERY_SERVICE_NAME = 'pitchup_discovery'
USER_COLLECTION_NAME_TEMPLATE = 'user_{}_pitch_{}'

class Discovery(object):
    def __init__(self):
        self.discovery = DiscoveryV1(
            version=os.getenv('DISCOVERY_VERSION'),
            url=os.getenv('DISCOVERY_URL'),
            username=os.getenv('DISCOVERY_USERNAME'),
            password=os.getenv('DISCOVERY_PASSWORD')
        )

        # Get the Discovery service ID, if not found, create it.
        envs = self.getEnvironments()

        self.environment_id = False
        for env in envs['environments']:
            if env['name'] == PITCHUP_DISCOVERY_SERVICE_NAME:
                self.environment_id = env.get('environment_id', False)
                print("Found environment")
        
        if not self.environment_id:
            env = self.createEnvironment(PITCHUP_DISCOVERY_SERVICE_NAME, "PitchUp Discovery Service Environment")
            self.environment_id = env.get('environment_id', False)

        if not self.environment_id:
            print("Failed to create Watson Discovery Service. Exiting.")
            exit()

    def createEnvironment(self, name, description):
        ''' Get the environments for this service '''

        env = self.discovery.create_environment(
            name=name,
            description=description
        ).get_result()

        return env


    def getEnvironments(self):
        ''' Get the environments for this service '''

        return self.discovery.list_environments().get_result()


    def createCollection(self, environment_id, name, description, lang='en'):
        ''' Create a collection to store documents '''

        new_collection = self.discovery.create_collection(
            environment_id=environment_id, 
            # configuration_id=configuration_id, 
            name=name, 
            description=description, 
            language=lang
        ).get_result()

        return new_collection

    def deleteCollection(self, user_id, pitch_id):
        ''' Delete a collection '''

        print("here")
        collection = self.getUserCollection(user_id, pitch_id)
        print("Type of collection:", type(collection))
        print(collection)

        if collection:
            resp = self.discovery.delete_collection(
                environment_id = self.environment_id,
                collection_id = collection['collection_id']
            )

            print(resp)

        return True


    def getSingleCollection(self, environment_id, collection_id, **kwargs):
        ''' Get a single collection '''

        collection = self.discovery.get_collection(environment_id, collection_id).get_result()

        return collection


    def getCollections(self, environment_id, name=None, **kwargs):
        ''' Gets all collections '''

        collection = self.discovery.list_collections(
            environment_id=environment_id,
            name=name
        ).get_result()

        return collection


    def getUserCollection(self, user_id, pitch_id):
        ''' Get a collection for a user given its ID '''

        collection = self.discovery.list_collections(
            environment_id = self.environment_id,
            name = USER_COLLECTION_NAME_TEMPLATE.format(user_id, pitch_id)
        ).get_result()

        if collection.get('collections', False):
            print("Found user collections:")
            col_list = collection.get('collections', False)
            return col_list[0]
        else:
            print("SECOND ELSE")
            return False
        

    def createUserCollection(self, user_id, pitch_id):
        ''' Create a collection for a user given its ID '''
        
        collection = self.createCollection(
            environment_id = self.environment_id,
            name = USER_COLLECTION_NAME_TEMPLATE.format(user_id, pitch_id),
            description = "User {}, Pitch {} - Discovery Docs Collection".format(user_id, pitch_id)
        )

        if collection.get('collections', False):
            return collection.get('collections', False)[0]
        else:
            return False


    def queryCollection(self, collection_id):
        ''' Query a collection '''

        # based on this:
        #https://gateway.watsonplatform.net/discovery/api/v1/environments/70fc388b-3358-4a63-aa02-946b3e1fb3aa/collections/24bd2e65-aa3f-43e5-8e35-f45b58208dcd/query?version=2018-08-01&aggregation=term%28enriched_text.concepts.text%2Ccount%3A10%29&deduplicate=false&highlight=true&passages=true&passages.count=5&query=
            
        query_response = self.discovery.query(
            environment_id = self.environment_id,
            collection_id = collection_id,
            count = 10,
            aggregation = 'term(enriched_text.concepts.text,count:10)'
        ).get_result()

        if query_response:
            return query_response.get('aggregations')
        else:
            return False

    
    def addDocument(self, user_id, pitch_id, collection_id, file_name):
        ''' Add a document to a collection '''

        file_path = os.path.join(FILESTORE_USER_DOCUMENT_TEMPLATE.format(user_id, pitch_id), file_name)

        # Make sure file exists        
        if not os.path.isfile(file_path):
            print("Could not find file at", file_path)
            return False

        else:
            
            print("Uploading", file_name, "to Discovery")

            try:

                with open(file_path, 'rb') as file_info:
                    add_doc = self.discovery.add_document(
                        environment_id = self.environment_id,
                        collection_id = collection_id,
                        file = file_info,
                        # TODO right now only allowing pdf because a plain .txt file failed and there's limited support types.
                        file_content_type= 'application/pdf',   
                        filename = file_name
                    ).get_result()

            except Exception as e:
                raise e

        return add_doc

if __name__ == '__main__':

    #init Watson
    wat = Discovery()  
    
    # At this point, we have our discovery_env_id
    user_id = '1'
    pitch_id = '1'
    user_collection = False

    # Check if a collection exists for the user, if not, make it
    user_collection = wat.getUserCollection(user_id, pitch_id)

    if not user_collection:
        user_collection = wat.createUserCollection(user_id, pitch_id)

    print("User collection:", user_collection)
    user_collection_id = user_collection['collection_id']
