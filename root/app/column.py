from flask import render_template, request, redirect, url_for, Blueprint, current_app as app
from flask_login import login_required
from .data import input_info

columns = Blueprint(name='columns', import_name=__name__ , url_prefix='/columns')

# Server-side rendered
@columns.route('', methods=['GET'])
def get_columns():
  return render_template('columns/columns-main.html')

@columns.route('/editor', methods=['GET'])
def get_editor():
  return render_template('editor/editor.html', input_info=input_info)

@columns.route('/<id>', methods=['GET'])
def get_one_column(id):
  pass

# API
@columns.route('', methods=['POST'])
def create_column():
  pass

@columns.route('/upload', methods=['POST'])
def upload_image():
  pass

