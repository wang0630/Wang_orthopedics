# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
  # default: default value of the input
  username = StringField("Username", validators=[DataRequired(u"請輸入帳號"), Length(min=6, message=u"帳號太短了")])
  password = PasswordField("Password", validators=[DataRequired(u"請輸入密碼")])
  submit = SubmitField(u"登入")
