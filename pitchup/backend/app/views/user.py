from flask import Blueprint, render_template, jsonify

from app.database import db
from app.models import User


mod = Blueprint('user', __name__, url_prefix='/user')


@mod.route('/')
def index():
    new_user = User(name='Joe')
    db.session.add(new_user)
    db.session.commit()
    return 'hi'
