from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.trainer_app

collection_name = db["trainers_app"]