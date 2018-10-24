################################################################################
# Application configurations
#
#   Place any non-sensitive (API keys, etc) application constants and
#       configuraitons here
#
################################################################################

import os
from dotenv import load_dotenv

APP_NAME = 'PitchUp: Backend Application'
APP_VERSION = "0.0.1"
APP_ROOT = os.path.dirname(os.path.realpath(__file__))

SQLITE_DB_LOCATION = 'sqlite:///database/dev.db'
TEST_SQLITE_DB_LOCATION = 'sqlite:///database/test.db'


# Paths
FILESTORE_PATH = os.path.join(APP_ROOT, 'filestore')
FILESTORE_USER_DOCUMENT_ROOT = os.path.join(FILESTORE_PATH, 'user')
FILESTORE_USER_DOCUMENT_TEMPLATE = FILESTORE_USER_DOCUMENT_ROOT + '/user_{}/pitch_{}'


def get_environment_config(environment):
    ''' Return variables based on the requested environment '''

    conf = {}

    load_dotenv()

    if environment == 'DEVELOPMENT':
        conf['RDBMS_DATABASE_URI'] = SQLITE_DB_LOCATION
        conf['TESTING'] = False

    elif environment == 'TESTING':
        conf['RDBMS_DATABASE_URI'] = TEST_SQLITE_DB_LOCATION
        conf['TESTING'] = True

    else:
        conf = False

    return conf
