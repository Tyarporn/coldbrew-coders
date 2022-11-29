import pymongo as pm 
import os
from dotenv import load_dotenv

REMOTE = "0"
LOCAL = "1"

client = None
load_dotenv()


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    We should probably either return a client OR set a
    client global.
    """
    CONNECTION_STRING = os.getenv('connection_string')
    global client
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("connection_string", CONNECTION_STRING) == CONNECTION_STRING:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient(CONNECTION_STRING)


def insert_bot():
    pass


def delete_bot():
    pass


def insert_comment():
    pass


def delete_comment():
    pass


def query_bot_id(bot_id):
    mydb = client["coldbrew_coders"]
    mycol = mydb["bot_ids"]
    myquery = {"bot_id": bot_id}
    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)


if __name__ == "__main__":
    connect_db()
    query_bot_id("0460")
