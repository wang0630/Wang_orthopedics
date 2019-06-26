from werkzeug.security import check_password_hash
from flask_login import UserMixin

# Inherit from UserMixin to get basic implementation of the required functions
class Admini(UserMixin):
  def __init__(self, username):
    self.username = username
  # Override
  def get_id(self):
    return self.username
  @staticmethod
  def validate_password(password, input_password):
    return password == input_password