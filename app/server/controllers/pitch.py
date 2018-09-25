from flask import Blueprint, render_template, jsonify, request

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry

pitch_blueprint = Blueprint('pitch', __name__, url_prefix='/pitch')

@pitch_blueprint.route('/')
def index():
    return 'Pitch'
