import jinja2
from sys import path as sys_path
from os.path import join, dirname
from flask import Flask
from flask_login import LoginManager
from flask_compress import Compress
from pathlib import Path

# Imporant!!!
# Make /wang-orthopedics/app be in the path of sys.path
# So we can import siblings package
sys_path.append(join(dirname(__file__)))

# flask_loging setup
lm = LoginManager()

def create_app():
  # Create the app
  app = Flask(__name__, static_url_path='/static')

  # Import config after the dotenv
  from .config import Config

  app.config.from_object(Config)

  lm.init_app(app)
  # This view will be the one which users will be returned to when they try to access a protected route
  lm.login_view = 'auth.login'
  lm.login_message = u'你沒有權限進入這個頁面'

  from .main import main
  from .auth import auth
  from .announcements import announcements
  from .columns import columns
  from .errors import errors

  # register blueprint
  app.register_blueprint(main)
  app.register_blueprint(auth)
  app.register_blueprint(announcements)
  app.register_blueprint(errors)
  app.register_blueprint(columns)

  my_loader = jinja2.ChoiceLoader([
      app.jinja_loader,
      # Load templates from app/template, so all html files can use relative path to refet to each other
      jinja2.FileSystemLoader(['/app/template/']),
    ])
  app.jinja_loader = my_loader

  def concat_lists(a, b):
    return [*a, *b]

  # Add customed filters by adding our functions to DEFAULT_FILTERS object
  jinja2.environment.DEFAULT_FILTERS['concat_lists'] = concat_lists

  # Import static assets
  from .assets import create_assets
  create_assets(app)

  # Enable gzip by using flask-compress
  Compress(app)
  return app
