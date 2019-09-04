from math import ceil

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
  for a in announcements:
    a['date'] = f"{a['date'].year}/{a['date'].month}/{a['date'].day}"
  total_pages = ceil(len(announcements) / per_page)
  print(announcements)
  return announcements, total_pages

def post_announcement(collection, announcement):
  print(announcement)
  result = collection.insert_one(announcement)
  return result.inserted_id
