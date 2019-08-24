from math import ceil

def fetch_all_announcements(collection, per_page):
  agg = collection.aggregate([
    {
      '$project': {
        '_id': 0,
        'content': 1,
        'date': 1,
        'id': {
          '$toString': '$_id'
        }
      }
    }
  ])
  announcements = list(agg)
  total_pages = ceil(len(announcements) / per_page)
  return list(agg), total_pages
