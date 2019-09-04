import os
from pymongo import MongoClient

class Config:
  APIKEY = os.environ.get('APIKEY')
  # For CSRF protection
  SECRET_KEY = os.environ.get('SECRET_KEY')
  # db config
  DB_NAME = 'clinic'
  MONGO_URL = os.environ.get('MONGO_URL')
  MONGO_DB = MongoClient(MONGO_URL)[DB_NAME]
  MONGO_COLLECTION_ADMINI = MONGO_DB['admini']
  MONGO_COLLECTION_ANNOUNCEMENT = MONGO_DB['announcement']
  # Some constant
  AC_PER_PAGE = 4
  # Development
  ENV=os.environ.get('FLASK_ENV')
  REQUEST_IP=os.environ.get('LOCALHOST') if ENV == 'development' else os.environ.get('PUBLICHOST')
  
