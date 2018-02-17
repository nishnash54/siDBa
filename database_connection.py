#MongoDB connection
from pymongo import MongoClient

def update_database(dblink, database_name, collection_name, data):
    print dblink
    try:
        client = MongoClient(dblink)
        db = client[database_name]
        eval("db." + str(collection_name) + ".insert_many(data)")
        return {"code": 200, "msg": "Collection added to database"}
    except:
        return {"code": 400, "msg": "Connection cannot be estb."}
