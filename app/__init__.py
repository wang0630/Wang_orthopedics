import jinja2
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from pathlib import Path

# Load environ variables from external file
# __file__ represents the abs path of this file
# parents[1] goes one level up to root folder
env_path = Path(__file__).parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

# Create the app
app = Flask(__name__, static_url_path='/static')

# Import config after the dotenv
from .config import Config
app.config.from_object(Config)

# flask_loging setup
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'auth.login'

from .main import main
from .auth import auth
from .announcements import announcements
# register blueprint
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(announcements)

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    # Load templates from app/template, so all html files can use relative path to refet to each other
    jinja2.FileSystemLoader(['/app/template/']),
  ])
app.jinja_loader = my_loader

from . import assets
