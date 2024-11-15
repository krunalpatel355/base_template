from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from flask import current_app
import os

def init_mongo():
    try:
        # Get MongoDB connection details from environment variables
        mongo_host = os.getenv('MONGO_HOST', 'localhost')
        mongo_user = os.getenv('MONGO_USER')
        mongo_pass = os.getenv('MONGO_PASS')  # Fixed typo in MONGO_aPASS
        mongo_db = os.getenv('MONGO_DB', 'flask_app')
        
        # Construct MongoDB URI
        if mongo_user and mongo_pass:
            mongo_uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}/{mongo_db}"
        else:
            mongo_uri = f"mongodb://{mongo_host}/{mongo_db}"
            
        # Create MongoDB client
        client = MongoClient(mongo_uri)
        
        # Test connection
        client.admin.command('ping')
        
        return client[mongo_db]
        
    except ConnectionFailure as e:
        current_app.logger.error(f"Could not connect to MongoDB: {e}")
        raise

# Initialize the mongo client
mongo = init_mongo()