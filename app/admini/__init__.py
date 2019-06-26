from werkzeug.security import check_password_hash
from flask_login import UserMixin

# Inherit from UserMixin to get basic implementation of the required functions
class Admini(AdminiMixin):
  def __init__(self, username):
    self.username = username
  @staticmethod
    def validate_password(password, input_password):
      return password == input_password