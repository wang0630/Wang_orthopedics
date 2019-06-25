from flask_assets import Environment,Bundle
from . import app
import os

assets = Environment(app)

assets.load_path = [
  os.path.join(os.path.dirname(__file__), "static", "Sass")
]

assets.register(
  "css_all",
  Bundle("main.scss",
          filters="pyscss,cssmin",
          depends="**/*.scss",
          output="css/style.css")
)