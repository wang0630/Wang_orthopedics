import os
from pymongo import MongoClient

class Config:
  APIKEY = os.environ.get("APIKEY")
  # For CSRF protection
  SECRET_KEY = 'my fucking key'
  # db config
  DB_NAME = 'clinic'
  MONGO_URL = "mongodb+srv://j2081499:s3353830@wang-clinic-ff80a.mongodb.net/test?retryWrites=true&w=majority"
  MONGO_DB = MongoClient(MONGO_URL)[DB_NAME]
  MONGO_COLLECTION_ADMINI = MONGO_DB['admini']
  MONGO_COLLECTION_ANNOUNCEMENT = MONGO_DB['announcement']