################################################################################
# PitchUp Mockup
#
# A quick mockup for pitchup.
#
# To run... "python run.py"
#
################################################################################


from bottle import route, run, template, static_file

# Static files
@route('/assets/<filepath:path>')
def assets_static(filepath):
    return static_file(filepath, root='assets/')

@route('/dist/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='dist/')

# Add any routes manually here
@route('/')
def index():
    return template('index')

@route('/dashboard')
def dashboard():
    return template('dashboard')

@route('/recording')
def recording():
    return template('recording')

@route('/recording_summary/<id>')
def recording_summary(id):
    return template('recording_summary', id=id)

@route('/analyzing')
def analyzing():
    return template('analyzing')

@route('/results')
def results():
    return template('results')

@route('/new')
def new():
    return template('recording')

@route('/new_pitch')
def new_pitch():
    return template('new_pitch')



# Run the application
run(host='localhost', port='8080', debug=True, reloader=True)