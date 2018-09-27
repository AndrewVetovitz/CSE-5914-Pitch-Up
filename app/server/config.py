################################################################################
# Application configurations
#
#   Place any non-sensitive (API keys, etc) application constants and
#       configuraitons here
#
################################################################################

import os

APP_NAME = 'PitchUp: Backend Application'
APP_VERSION = "0.0.1"
APP_ROOT = os.path.dirname(os.path.realpath(__file__))

SQLITE_DB_LOCATION = 'sqlite:///database/dev.db'


# Paths
FILESTORE_PATH = os.path.join(APP_ROOT, 'filestore')
FILESTORE_USER_DOCUMENT_ROOT = os.path.join(FILESTORE_PATH, 'user')
FILESTORE_USER_DOCUMENT_TEMPLATE = FILESTORE_USER_DOCUMENT_ROOT + '/user_{}/pitch_{}'