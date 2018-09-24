from flask import Blueprint, request
user_blueprint = Blueprint('user', __name__, template_folder=None)

from helpers.authentication import requires_auth

@user_blueprint.route('/login')
def loginUser():
    email  = request.args.get('email', None)
    password  = request.args.get('password', None)

    return email + ' ' + password

@user_blueprint.route('/<user>')
@requires_auth
def getUser(user):
    return user + '!!!!!!'
