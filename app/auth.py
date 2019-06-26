from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user
from . import lm, app
from .admini import Admini
from .loginForm.loginForm import LoginForm

auth = Blueprint('auth', __name__)

# main login page
# must loggin to see the page
@auth.route('/loginMain')
@login_required
def login_main():
  return render_template('login/loginMain.html')


# Login form
@auth.route('/login', methods=['GET', 'POST'])
def login():
  # Create the form
  form = LoginForm()
  print(form.username.data)
  print(form.password.data)
  if not form.validate_on_submit():
    # All fields must be validated when submit btn is clicked
    return render_template('login/loginForm.html', form=form)
  
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
  admini = app.config['MONGO_COLLECTION_ADMINI'].find_one({'username': username})
  if not admini:
      return None
  return User(admini['username'])
