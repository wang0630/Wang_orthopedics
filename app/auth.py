from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user, current_user
from math import ceil
from . import lm, app
from .admini import Admini
from .loginForm.loginForm import LoginForm

auth = Blueprint('auth', __name__)

# main login page
# must loggin to see the page
@auth.route('/loginMain', methods=['GET'])
@login_required
def login_main():
  AC_PER_PAGE = 4
  # Fetch existing announcement from db
  # transform Objectid to string
  agg = app.config['MONGO_COLLECTION_ANNOUNCEMENT'].aggregate([
    {
      '$project': {
        '_id': 0,
        'content': 1,
        'date': 1,
        'id': {
          '$toString': '$_id'
        }
      }
    }
  ])
  announcements = list(agg)
  # Page the list per 4 announcements
  total_pages = ceil(len(announcements) / 4)
  return render_template('login/loginMain.html', ac_per_page=AC_PER_PAGE, announcements=announcements, total_pages=total_pages)

# Login form
@auth.route('/login', methods=['GET', 'POST'])
def login():
  # Create the form
  form = LoginForm()

  # current_user is a proxy for current login user
  # it will be an anonymous user if he is not logged in
  # anonymous user will return None when get_id() is called
  idd = current_user.get_id()
  if request.method == 'GET':
    print('here in GET')
    if idd:
      print(f"current_user.get_id(): {idd}")
      return redirect(url_for('.login_main'))
    else:
      return render_template('login/loginForm.html', form=form)
  else: # post request
    if not form.validate_on_submit():
      # All fields must be validated when submit btn is clicked
      # Or the method is get
      # simply return loginForm.html
      return render_template('login/loginForm.html', form=form)

    # Fetch the db to get the admini
    admini_doc = app.config['MONGO_COLLECTION_ADMINI'].find_one({'username': form.username.data})
    print(f"find a admini {admini_doc}")

    # Check if admini exists and the password
    if not admini_doc or not Admini.validate_password(admini_doc['password'], form.password.data):
      # Password is not correct or admini name not exists
      return render_template('login/loginForm.html', form=form)
    
    admini_obj = Admini(admini_doc['username'])
    # Login the user
    login_user(admini_obj)
    return redirect(url_for('.login_main'))


# Reload the user object through different session
# return User obj if the ID is valid
# return None if the ID is not valid
@lm.user_loader
def load_user(username):
  admini_obj = app.config['MONGO_COLLECTION_ADMINI'].find_one({'username': username})
  if not admini_obj:
      return None
  return Admini(admini_obj['username'])
