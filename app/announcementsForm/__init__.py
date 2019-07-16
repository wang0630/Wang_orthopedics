from flask_wtf import FlaskForm
from wtforms import DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class AnnouncementsForm(FlaskForm):
  date = DateField(u'日期', validators=[DataRequired(u'請輸入日期')])
  title = SelectField(u'公告種類', choices=[(u'general', u'一般公告'), (u'adjust', u'服務更改'), (u'schedule', u'看診時刻調整')])
  content = TextAreaField(u'公告內容', validators=[DataRequired(u'公告不能為空白'), Length(max=50, message=u'公告不能長於50字')])