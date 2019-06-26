import os

class Config:
  APIKEY = os.environ.get("APIKEY")
  # For CSRF protection
  SECRET_KEY = 'my fucking key'