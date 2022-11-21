from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('db_username') # get username and password
PASSWORD = os.getenv('db_password')
CONNECTION_STRING = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.wux8g.mongodb.net/?retryWrites=true&w=majority' # get connection string
client = MongoClient(CONNECTION_STRING) # establish client

def query_id():
   # Create the database for our example (we will use the same database throughout the tutorial
   mydb = client["coldbrew_coders"] # get specific database
   mycol = mydb["bot_ids"] # get specific column
#    print(mycol)
   myquery = { "bot_id": "0460" } # find document with bot id like 0460
   mydoc = mycol.find(myquery)

   for x in mydoc:
    print(x) 
   return 

  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
   query_id()