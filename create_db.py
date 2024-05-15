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


# Виведення всіх записів із колекції
def read_all_cats():
    return list(cats_collection.find({}))

# Виведення інформації про кота за ім'ям
def read_cat_by_name(cat_name):
    return cats_collection.find_one({"name": cat_name})

# Оновити вік кота за ім'ям
def update_cat_age(cat_name, new_age):
    cats_collection.update_one({"name": cat_name}, {"$set": {"age": new_age}})

# Додати нову характеристику до списку features кота за ім'ям
def add_cat_feature(cat_name, new_feature):
    cats_collection.update_one({"name": cat_name}, {"$push": {"features": new_feature}})

# Видалення запису з колекції за ім'ям
def delete_cat_by_name(cat_name):
    cats_collection.delete_one({"name": cat_name})

# Видалення всіх записів із колекції
def delete_all_cats():
    cats_collection.delete_many({})
