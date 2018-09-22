################################################################################
# Application driver
#
#   To run application from shell: python app.py
#
################################################################################

from flask import Flask

def create_app():

    from app.database import db
    from config import SQLITE_DB_LOCATION
    from app.views import user

    # App object
    app = Flask(__name__)

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_LOCATION
    db.init_app(app)

    # Views/Blueprints
    app.register_blueprint(user.mod)

    return app


if __name__ == "__main__":

    app = create_app()
    app.run(debug=True, port=5000)
