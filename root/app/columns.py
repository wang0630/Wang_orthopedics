from os.path import join, dirname
from datetime import datetime
from uuid import uuid4
from bson.objectid import ObjectId
from flask import render_template, request, make_response, redirect, url_for, Blueprint, Markup,current_app as app
from flask_login import login_required
import werkzeug.exceptions as WE
from w3lib.url import parse_data_uri
from boto3 import client
from botocore.exceptions import ClientError
from .data import input_info
from .dbService import fetch_columns_info_by_page
from .dbService.helpers import insert_single_doc, get_collection_count, fetch_one_doc, fetch_docs
from helpers.html_multipulate import traverse_insert_img_src
import helpers.cookie as cookie_lib

columns = Blueprint(name='columns', import_name=__name__ , url_prefix='/columns')

# Server-side rendered
@columns.route('', methods=['GET'])
def get_columns():
  # Get query string, default to 1
  page = int(request.args.get('page', 1))
  # One page has 4 Columns
  per_page = 4
  count = get_collection_count(app.config['MONGO_COLLECTION_COLUMN'])
  # Pagination according to the page string
  columns_info = fetch_columns_info_by_page(app.config['MONGO_COLLECTION_COLUMN'], page, per_page)
  # Fetch name and author by cookie
  cookie = request.cookies.get('recent_view')
  recent_view_info = []
  if cookie:
    cookie_list = [ ObjectId(_id) for _id in cookie.split('&')]
    recent_view_info = fetch_docs(
      app.config['MONGO_COLLECTION_COLUMN'],
      { '_id': { '$in': cookie_list } },
      { 'content': 0, 'imgurl': 0, 'date': 0 },
    )
    for r in recent_view_info:
      r['_id'] = str(r['_id'])
  pagination_info = {
    'current_page': page,
    'count': count,
    'per_page': per_page,
  }
  return render_template('columns/columns.jinja2', columns_info=columns_info, recent_view_info=recent_view_info, pagination_info=pagination_info)

@columns.route('/editor', methods=['GET'])
def get_editor():
  return render_template(
    'editor/editor.jinja2',
    input_info=input_info,
    request_ip=app.config['REQUEST_IP'],
    editor_post_limit=app.config['EDITOR_POST_LIMIT']
    )

@columns.route('/<id>', methods=['GET'])
def get_one_column(id):
  if ObjectId.is_valid(id):
    # Fetch the document
    column_doc = fetch_one_doc(
      app.config['MONGO_COLLECTION_COLUMN'],
      { '_id': ObjectId(id) },
      { '_id': 0 },
      )
    if not column_doc:
      WE.abort(404)
    # Traverse through the img and insert the src
    column_doc['content'] = traverse_insert_img_src(column_doc['content'], column_doc['imgurl'], app.config['AWS_S3_DOMAIN'])
    # Mark the html as safe, so jinja2 will not escape it
    column_doc['content'] = Markup(column_doc['content'])
    # Set cookie if this id is not present
    res = make_response(render_template(
      'columns/column_show.jinja2',
      column_doc=column_doc
    ))
    cookie_lib.test_and_set_cookie(res, request.cookies.get('recent_view'), id)
    return res
  else:
    # Raise 404 directly
    WE.abort(404)


# API
@columns.route('', methods=['POST'])
def create_column():
  try:
    # Accept incoming msg
    if (request.is_json):
      # Create object
      post = {
        'title': request.json.get('title'),
        'author': request.json.get('author'),
        'base64s': request.json.get('base64s'),
        'content': request.json.get('content'),
      }
      try:
        post_document = {
          'title': request.json.get('title'),
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
              raise WE.BadRequest('The img should be jpeg or png')
        # Insert the column into DB
        insert_single_doc(app.config['MONGO_COLLECTION_COLUMN'], post_document)
        return '', 204
      except ValueError as e:
        raise ValueError(e.args[0])
    else:
      raise WE.NotAcceptable('Request should have MIME type of application/json')
  except Exception as e:
    print(e)
    WE.abort(500)


# Error handling
@columns.errorhandler(WE.BadRequest)
def bad_request(e):
  return e.description, 400

@columns.errorhandler(WE.NotFound)
def not_found(e):
  return 'OOPS, 找不到這篇專欄喔！', 404

@columns.errorhandler(WE.NotAcceptable)
def not_acceptable(e):
  return e.description, 406

@columns.errorhandler(WE.InternalServerError)
def internal_server_error(e):
  print(e.description)
  return 'OOPS, 伺服器有些問題，請稍後再試！', 500
