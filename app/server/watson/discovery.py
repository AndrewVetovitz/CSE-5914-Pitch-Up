import os
import json
from watson_developer_cloud import DiscoveryV1

from config import APP_ROOT, FILESTORE_PATH, FILESTORE_USER_DOCUMENT_ROOT, FILESTORE_USER_DOCUMENT_TEMPLATE

# APP_ROOT = '/home/zizonia/dev/college/5914/CSE-5904-Pitch-Up/app/server'
# FILESTORE_PATH = os.path.join(APP_ROOT, 'filestore')
# FILESTORE_USER_DOCUMENT_ROOT = os.path.join(FILESTORE_PATH, 'user')
# FILESTORE_USER_DOCUMENT_TEMPLATE = FILESTORE_USER_DOCUMENT_ROOT + '/user_{}/pitch_{}'

PITCHUP_DISCOVERY_SERVICE_NAME = 'pitchup_discovery'
USER_COLLECTION_NAME_TEMPLATE = 'user_{}_pitch_{}'

class Discovery(object):

    def __init__(self):
        print(os.getenv('DISCOVERY_VERSION'))
        self.discovery = DiscoveryV1(
            version = os.getenv('DISCOVERY_VERSION'),
            url = os.getenv('DISCOVERY_URL'),
            username = os.getenv('DISCOVERY_USERNAME'),
            password = os.getenv('DISCOVERY_PASSWORD')
        )

        # Get the Discovery service ID, if not found, create it.
        envs = self.getEnvironments()

        self.environment_id = False
        for env in envs['environments']:
            if env['name'] == PITCHUP_DISCOVERY_SERVICE_NAME:
                self.environment_id = env.get('environment_id', False)
                print("Found environment")
        
        if not self.environment_id:
            env = wat.createEnvironment(PITCHUP_DISCOVERY_SERVICE_NAME, "PitchUp Discovery Service Environment")
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
            col_list = collection.get('collections', False)
            return col_list[0]
        else:
            return False
        

    def createUserCollection(self, user_id, pitch_id):
        ''' Create a collection for a user given its ID '''
        
        collection = self.createCollection(
            environment_id = self.environment_id,
            name = USER_COLLECTION_NAME_TEMPLATE.format(user_id, pitch_id),
            description = "User {}, Pitch {} - Discovery Docs Collection".format(user_id, pitch_id)
        ).get_result()

        if collection:
            return collection.get('collections', False)[0]
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

    # Upload a document to collection
    file_path = ''
    file_name = 'test.pdf'
    wat.addDocument(user_id, pitch_id, user_collection_id, file_name)
