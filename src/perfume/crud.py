from src.perfume.model import PerfumeInDB
from db import collection
from bson import ObjectId

async def create_perfume(perfume: PerfumeInDB):
    result = await collection.insert_one(perfume.to_bson())
    return str(result.inserted_id)

async def get_perfume(perfume_id: str):
    document = await collection.find_one({"_id": ObjectId(perfume_id)})
    if document:
        document['_id'] = str(document['_id'])
    return document

async def get_page_of_perfumes(page: int, page_size: int):
    cursor = collection.find().skip(page * page_size).limit(page_size)
    documents = await cursor.to_list(length=page_size)
    for document in documents:
        document['_id'] = str(document['_id'])
    return documents

async def update_perfume(id: str, parfume: PerfumeInDB):
    result = await collection.find_one_and_update({"_id": id}, {"$set": parfume.dict()}, return_document=True)
    if result:
        result['_id'] = str(result['_id'])
    return result

async def delete_perfume(perfume_id: str):
    result = await collection.find_one_and_delete({"_id": ObjectId(perfume_id)})
    if result:
        result['_id'] = str(result['_id'])
    return result



# 357394658684-tvhsd8709fuoeitnb27mld3gba1bs68b.apps.googleusercontent.com