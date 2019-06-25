from flask import Flask
from flask_assets import Environment,Bundle
from .config import Config
app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
from app import route
from . import assets