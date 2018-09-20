from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controllers.user import user_blueprint
from controllers.report import report_blueprint


SQLITE_DB_LOCATION = 'sqlite:///db/test.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_LOCATION
db = SQLAlchemy(app)

app.register_blueprint(user_blueprint)

if __name__ == "__main__":

    app.run(debug=True, port=5000)
