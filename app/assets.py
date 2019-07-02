import os
from flask_assets import Environment,Bundle
from . import app

assets = Environment(app)

# Let flask_assets can find the path of Scss and Js files
assets.load_path = [
  os.path.join(os.path.dirname(__file__), 'static', 'src', 'Sass'),
  os.path.join(os.path.dirname(__file__), 'static', 'src', 'Js'),
]

bundles = {
  'css-all': Bundle('main.scss',
          filters='pyscss,cssmin',
          depends='**/*.scss',
          output='css/style.css'),

  'js-main': Bundle('js-main.js',
                    filters='jsmin',
                    output='js/js-main.js')
}

assets.register(bundles)
