from flask import render_template, request, redirect, url_for, Blueprint
from .loginForm.loginForm import LoginForm

auth = Blueprint("auth", __name__)

# main login page
@auth.route("/loginMain")
def login():
  return render_template("login/loginMain.html")


# Login form
@auth.route("/loginForm", methods=["GET", "POST"])
def loginForm():
  # Create the form
  form = LoginForm()
  print(form.username.errors)
  print(form.password.errors)
  if not form.validate_on_submit():
    # All fields correct when submit btn is clicked
    print('helllooo')
    return render_template("login/loginForm.html", form=form)
  # Login succeed, redirect to loginMain
  return redirect(url_for("login"))
