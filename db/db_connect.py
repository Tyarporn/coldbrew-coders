import pymongo as pm
import os
from dotenv import load_dotenv


COLDBREW_DB = "coldbrew_coders"
client = None


def connect_db():
    global client

    load_dotenv()
    CONNECT_STR = os.getenv('connection_string')
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("connection_string", CONNECT_STR) == CONNECT_STR:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient(CONNECT_STR)


def insert_one(collection, doc, db=COLDBREW_DB):
    """
    Insert a single doc into collection.
    """
    client[db][collection].insert_one(doc)

def update_one(collection, filt, new_values, db=COLDBREW_DB):
    """
    Updates a single doc into collection.
    """
    client[db][collection].update_one(filt, new_values)


def fetch_one(collection, filt, db=COLDBREW_DB):
    """
    Find with a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
        return doc


def del_one(collection, filt, db=COLDBREW_DB):
    """
    Find with a filter and return on the first doc found.
    """
    client[db][collection].delete_one(filt)


def fetch_all(collection, db=COLDBREW_DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=COLDBREW_DB):
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret


if __name__ == "__main__":
    connect_db()
    print(fetch_one('user', {'username': 'tyarporn'}))
