from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client.get_database('app')
strains_collection = db['Strains']
strains_records = list(strains_collection.find({'isStub': False}))

if __name__ == "__main__":
    print("DB: ", db)

    print("strains count: ",
          strains_collection.count_documents({'isStub': False}))

    print("first strain name", strains_records[0]['name'])
