from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user, current_user
from bson import ObjectId
from .announcementsForm import AnnouncementsForm
from .dbService import fetch_all_announcements
from . import app

announcements = Blueprint(name='announcements', import_name=__name__ , url_prefix='/announcement')

@announcements.route('/<id>', methods=['DELETE'])
@login_required
def deletion(id):
  objId = ObjectId(id)
  deleted = app.config['MONGO_COLLECTION_ANNOUNCEMENT'].find_one_and_delete({ '_id': objId })
  # print(id)
  if deleted:
    return 'Deletion succeeds', 200
  else:
    return 'Deletion fails, query not found', 404

@announcements.route('', methods=['POST'])
@login_required
def post():
  form = AnnouncementsForm()
  error_msgs = []
  if not form.validate_on_submit():
    if (form.date.errors):
      error_msgs.append(u'日期不符合格式，請重新輸入！')
      announcements, total_pages = \
        fetch_all_announcements(app.config['MONGO_COLLECTION_ANNOUNCEMENT'], app.config['AC_PER_PAGE'])
    # Bad request
    return render_template(
        'login/loginMain.html',
        form=form,
        ac_per_page=app.config['AC_PER_PAGE'],
        announcements=announcements,
        total_pages=total_pages,
        request_ip=app.config['REQUEST_IP']
      ), 400
  else:
    return '', 204


# For preflight aka CORS
@announcements.after_request
@login_required
def after_request(res):
  if request.method == 'OPTIONS':
    header = res.header
    print(f'Original header: {header}')
    header['Access-Control-Allow-Methods'] = ['GET', 'POST', 'DELETE']
    header['Access-Control-Allow-Headers'] = '*'
  
  return res