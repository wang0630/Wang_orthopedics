def insert_single_doc(collection, target_doc):
  print(target_doc)
  result = collection.insert_one(target_doc)
  return result.inserted_id

def get_collection_count(collection):
  return collection.estimated_document_count()
