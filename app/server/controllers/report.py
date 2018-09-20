from flask import Blueprint, request
report_blueprint = Blueprint('report', __name__, template_folder=None)

@report_blueprint.route('/report/<id>')
def get_report():

    return 'report' + str(id)
