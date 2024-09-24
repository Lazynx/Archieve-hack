from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)

db = client.perfume

collection = db.get_collection("perfume")
