from flask import Blueprint, request

from database import db

report_blueprint = Blueprint('report', __name__, template_folder=None)

@report_blueprint.route('/report/<id>')
def get_report():
    ''' Returns a single report by id if it exists '''
    
    return 'report' + str(id)
