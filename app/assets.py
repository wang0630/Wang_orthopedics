import os
from flask_assets import Environment,Bundle
from . import app

assets = Environment(app)

# Let flask_assets can find the path of Scss file
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