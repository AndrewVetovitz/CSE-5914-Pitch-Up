from flask import Blueprint
from six.moves.urllib.parse import urlencode

user_blueprint = Blueprint('user', __name__, template_folder=None)

from helpers.authenticate import requires_auth

@user_blueprint.route('/<user>')
@requires_auth
def getUser(user):
    # Get user info here
    return user

@requires_auth
def upload(user, info):
    pass
