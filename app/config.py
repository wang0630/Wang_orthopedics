import os
from pymongo import MongoClient

class Config:
  APIKEY = os.environ.get("APIKEY")
  # For CSRF protection
  SECRET_KEY = os.environ.get('SECRET_KEY')
  # db config
  DB_NAME = 'clinic'
  MONGO_URL = f"mongodb+srv://{os.environ.get('MONGO_ACCOUNT')}:{os.environ.get('MONGO_PASSWORD')}@wang-clinic-ff80a.mongodb.net/test?retryWrites=true&w=majority"
  MONGO_DB = MongoClient(MONGO_URL)[DB_NAME]
  MONGO_COLLECTION_ADMINI = MONGO_DB['admini']
  MONGO_COLLECTION_ANNOUNCEMENT = MONGO_DB['announcement']
  # Development
  ENV='development'