from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Підключення до MongoDB
client = MongoClient(
    "mongodb+srv://koshelevskiyv:GOIT2024_Zp@goitlearn.1laswll.mongodb.net/",
    server_api=ServerApi("1"),
)

# Вибір або створення бази даних
db = client.cats_db

# Вибір або створення колекції
cats_collection = db.cats

# Створення даних колекції
cats_data = [
    {
        "name": "Barsik",
        "age": 3,
        "features": ["walks in slippers", "likes to be petted", "red"],
    },
    {"name": "Murka", "age": 2, "features": ["likes milk", "sleeps a lot", "gray"]},
    {"name": "Murzik", "age": 5, "features": ["angry", "stinker", "sleeps a lot"]},
]

# Вставка документів у колекцію
cats_collection.insert_many(cats_data)
