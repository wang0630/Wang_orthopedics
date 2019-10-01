from math import ceil
from helpers.convert_date import convert_date_to_roc

def fetch_all_announcements(collection, per_page):
  agg = collection.aggregate([
    {
      '$project': {
        '_id': 0,
        'content': 1,
        'date': 1,
        "title": 1,
        'id': {
          '$toString': '$_id'
        }
      }
    }
  ])
  announcements = list(agg)
  convert_date_to_roc(announcements)
  total_pages = ceil(len(announcements) / per_page)
  print(announcements)
  return announcements, total_pages

def fetch_columns_info(collection, page):
  PER_PAGE = 4
  agg = collection.aggregate([
    {
      '$skip': PER_PAGE * (page - 1)
    },
    {
      '$limit': PER_PAGE
    },
    {
      '$addFields': {
        'id': {
          '$toString': '$_id'
        } 
      }
    },
    {
      '$project': {
        '_id': 0,
        'content': 0,
        'imgurl': 0,
      }
    }
  ])
  columns = list(agg)
  convert_date_to_roc(columns)
  return columns


def insert_single_doc(collection, target_doc):
  print(target_doc)
  result = collection.insert_one(target_doc)
  return result.inserted_id

def get_collection_count(collection):
  return collection.estimated_document_count()
