from flask import render_template, request, redirect, url_for, Blueprint, current_app as app
from flask_login import login_required
from w3lib.url import parse_data_uri
from .data import input_info

columns = Blueprint(name='columns', import_name=__name__ , url_prefix='/columns')

# Server-side rendered
@columns.route('', methods=['GET'])
def get_columns():
  return render_template('columns/columns-main.html')

@columns.route('/editor', methods=['GET'])
def get_editor():
  return render_template(
    'editor/editor.html',
    input_info=input_info,
    request_ip=app.config['REQUEST_IP'],
    editor_post_limit=app.config['EDITOR_POST_LIMIT']
    )

@columns.route('/<id>', methods=['GET'])
def get_one_column(id):
  pass

# API
@columns.route('', methods=['POST'])
def create_column():
  # Accept incoming msg
  if (request.is_json):
    # Create object
    post = {
      'author': request.json.get('author'),
      'base64s': request.json.get('base64s'),
      'content': request.json.get('content'),
    }
    try:
      # Convert base64 img to real img
      for base64 in post['base64s']:
        result = parse_data_uri(base64)
        print(result[0])
    except ValueError:
      return 'The img format is not allowed', 400

    return '', 204
  else:
    return 'Request should be json', 400
  
  
  # upload to aws
  # return successful

@columns.route('/upload', methods=['POST'])
def upload_image():
  pass

