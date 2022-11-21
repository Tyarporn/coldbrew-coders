from pymongo import MongoClient
import os
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo

   CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster0.wux8g.mongodb.net/?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   print(client)
   return client['coldbrew_db']

  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()