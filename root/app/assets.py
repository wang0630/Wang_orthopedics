import os
from flask_assets import Environment,Bundle


def create_assets(app):
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
                      output='js/js-main.js'),

    'js-mutation-observer': Bundle('js-mutation-observer.js',
                                    filters='jsmin',
                                    output='js/js-mutation-observer.js'),
    'js-announcements': Bundle('js-announcements.js',
                                    filters='jsmin',
                                    output='js/js-announcements.js'),
    'js-lazy-loading':  Bundle('js-lazy-loading.js',
                                    filters='jsmin',
                                    output='js/js-lazy-loading.js'),
    'js-editor':  Bundle('js-editor.js',
                                    filters='jsmin',
                                    output='js/js-editor.js'),
    'js-pagination-arrow': Bundle('js-pagination-arrow.js',
                                    filters='jsmin',
                                    output='js/js-pagination-arrow.js'),
    'js-show-panel': Bundle('js-show-panel.js',
                                    filters='jsmin',
                                    output='js/js-show-panel.js'),                                                                       
  }

  assets.register(bundles)
