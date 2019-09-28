from os.path import join, dirname
from datetime import datetime
from uuid import uuid4
from flask import render_template, request, redirect, url_for, Blueprint, current_app as app
from flask_login import login_required
from w3lib.url import parse_data_uri
from boto3 import client
from botocore.exceptions import ClientError
from .data import input_info
from .dbService import insert_single_doc, fetch_columns_info

columns = Blueprint(name='columns', import_name=__name__ , url_prefix='/columns')

# Server-side rendered
@columns.route('', methods=['GET'])
def get_columns():
  # Get query string, default to 1
  page = int(request.args.get('page', 1))
  # Pagination according to the page string
  columns_info = fetch_columns_info(app.config['MONGO_COLLECTION_COLUMN'], page)
  # Retrieve columns info from db
  return render_template('columns/columns.html', columns_info=columns_info)

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
  try:
    # Accept incoming msg
    if (request.is_json):
      # Create object
      post = {
        'author': request.json.get('author'),
        'base64s': request.json.get('base64s'),
        'content': request.json.get('content'),
      }
      try:
        post_document = {
          'author': request.json.get('author'),
          'content': request.json.get('content'),
          'date': datetime.today(),
          'imgurl': [],
        }
        if post['base64s']:
          # Connect to S3
          s3 = client(
            's3',
            aws_access_key_id=app.config['AWS_S3_KEY'],
            aws_secret_access_key=app.config['AWS_S3_SECRET']
          )
          # Convert base64 img to real img
          for base64 in post['base64s']:
            result = parse_data_uri(base64)
            if (result[0] == 'image/jpeg' or result[0] == 'image/png'):
              new_id = uuid4()
              extension = result[0][result[0].index('/') + 1:]
              file_name = f'img/{new_id}.{extension}'
              # Upload to aws S3
              s3.put_object(
                Body=result[2],
                Bucket=app.config['BUCKET_COLUMN'],
                Key=file_name,
                ContentType=result[0],
              )
              post_document['imgurl'].append(file_name)  
            else:
              raise ValueError('The img should be jpeg or png')
        # Insert the column into DB
        insert_single_doc(app.config['MONGO_COLLECTION_COLUMN'], post_document)
        return '', 204
      except ValueError as e:
        raise ValueError(e.args[0])
      except ClientError as e:
        print(e.args)
        return e.args[0], 500
    else:
      return 'Request should be json', 406
  except ValueError as e:
    return e.args[0], 400
  except KeyError as e:
    return e.args[0], 500
  except Exception as e:
    return e.args[0], 500
