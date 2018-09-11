from flask import Flask
from routes.user import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
