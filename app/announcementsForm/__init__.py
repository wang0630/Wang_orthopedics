from flask_wtf import FlaskForm
from datetime import date
from wtforms import DateField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

def dateValidator(form, field):
  print(field.data)

class AnnouncementsForm(FlaskForm):
  date = DateField(u'日期', default=date.today, format='%Y/%m/%d', validators=[dateValidator])
  title = SelectField(u'公告種類', choices=[(u'general', u'一般公告'), (u'adjust', u'服務更改'), (u'schedule', u'看診時刻調整')], validators=[DataRequired(u'請選一個選項')])
  content = TextAreaField(u'公告內容', validators=[DataRequired(u'公告不能為空白'), Length(max=50, message=u'公告不能長於50字')])
  submit = SubmitField(u"發布公告")
