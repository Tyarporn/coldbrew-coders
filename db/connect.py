from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()
USERNAME = os.getenv('db_username')
PASSWORD = os.getenv('db_password')
CONNECTION_STRING = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.wux8g.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING)


def query_id():
    mydb = client["coldbrew_coders"]
    mycol = mydb["bot_ids"]
    myquery = {"bot_id": "0460"}
    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)


if __name__ == "__main__":
    query_id()
