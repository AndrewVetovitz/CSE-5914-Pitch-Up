import os

from flask import Blueprint
from flask import request
from flask import current_app

from six.moves.urllib.parse import urlencode

user_blueprint = Blueprint('user', __name__, template_folder=None)

from helpers.authenticate import requires_auth

@user_blueprint.route('/<user>')
@requires_auth
def getUser(user):
    # Get user info here
    return user

@user_blueprint.route('/upload', methods=['GET', 'POST'])
# @requires_auth
def upload():
    file = request.files['file']
    filename = file.filename

    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    
    return ('', 200)
