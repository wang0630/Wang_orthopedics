from flask import Flask
from .config import Config
from .main import main
from .auth import auth
# from flask_assets import Environment,Bundle

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
# register blueprint
app.register_blueprint(main)
app.register_blueprint(auth)

# from app import route
from . import assets