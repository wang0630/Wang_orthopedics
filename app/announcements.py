from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user, current_user
from bson import ObjectId
from . import app

announcements = Blueprint(name='announcements', import_name=__name__ , url_prefix='/announcements')

@announcements.route('/deletion/<id>', methods=['DELETE'])
@login_required
def deletion(id):
  objId = ObjectId(id)
  deleted = app.config['MONGO_COLLECTION_ANNOUNCEMENT'].find_one_and_delete({ '_id': objId })
  if deleted:
    return 'Deletion succeeds', 200
  else:
    return 'Deletion fails, query not found', 404