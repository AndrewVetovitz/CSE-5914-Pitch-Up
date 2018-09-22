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
    from app.views import user
    app.register_blueprint(user.mod)

    return app