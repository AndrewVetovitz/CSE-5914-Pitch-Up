from flask import Blueprint, render_template, jsonify, request

from app.database import db
from app.models import Pitch, PitchTry


mod = Blueprint('pitch', __name__, url_prefix='/pitch')


@mod.route('/')
def index():
    
    return 'Pitch'
