import jinja2
from flask import Flask
from flask_login import LoginManager

from dotenv import load_dotenv
from pathlib import Path  # python3 only
from os.path import join, dirname
from os import environ
#env_path = join(dirname(__file__), '..', '.env')
env_path = Path(__file__).parents[1] / '.env'
print(Path(__file__).parents[1] / '.env')
load_dotenv(dotenv_path=env_path)

app = Flask(__name__, static_url_path='/static')
from .config import Config
app.config.from_object(Config)
print(environ.get('ii', 'nope'))
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
