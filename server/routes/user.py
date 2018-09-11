from flask import Blueprint
user_blueprint = Blueprint('user', __name__, template_folder=None)

@user_blueprint.route('/<user>')
def show(user):
    return user + '!!!!!!'