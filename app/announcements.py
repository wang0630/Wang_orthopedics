from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user, current_user
from . import app

announcements = Blueprint(name='announcements', import_name=__name__ , url_prefix='/announcements')

@announcements.route('/deletion/<id>', methods=['DELETE'])
@login_required
def deletion(id):
  print(f'id is {id}')
  return 'hello', 200