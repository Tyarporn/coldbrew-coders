import pymongo as pm
import os
from dotenv import load_dotenv

LOCAL = "0"
CLOUD = "1"


COLDBREW_DB = "coldbrew_coders"
client = None


def connect_db():
    """
    Connects to mongo database by using connection string in
    .env file and initializes a global client variable
    """
    global client

    load_dotenv()
    CONNECT_STR = os.getenv('connection_string')
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("CLOUD_MONGO", LOCAL) == CLOUD:
            print("Connecting to Mongo in the cloud.")
            client = pm.MongoClient(CONNECT_STR)
        else:
            LOCAL_CONNECT_STR = os.getenv('local_connection_string')
            print("Connecting to Mongo locally.")
            client = pm.MongoClient(LOCAL_CONNECT_STR)


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
    """
    Fetches all documents from a collection in database
    """
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=COLDBREW_DB):
    """
    Fetches all documents and groups by key
    """
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret


if __name__ == "__main__":
    connect_db()
    print(fetch_one('user', {'username': 'tyarporn'}))
