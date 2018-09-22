################################################################################
# Application driver
#
#   To run application from shell: python app.py
#
################################################################################

from flask import Flask

def create_app():

    # App object
    app = Flask(__name__)

    # Database
    from app.database import db
    from config import SQLITE_DB_LOCATION
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_LOCATION
    db.init_app(app)

    # Views/Blueprints
    from app.views import user, pitch
    app.register_blueprint(user.mod)
    app.register_blueprint(pitch.mod)

    return app


if __name__ == "__main__":

    app = create_app()
    app.run(debug=True, port=5000)
