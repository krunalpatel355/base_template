import os
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_mongo_connection():
    mongo_host = os.getenv('MONGO_HOST', 'localhost')
    mongo_user = os.getenv('MONGO_USER')
    mongo_pass = os.getenv('MONGO_PASS')
    mongo_db = os.getenv('MONGO_DB', 'flask_app')
    
    logger.debug(f"Testing connection to MongoDB at {mongo_host}")
    
    try:
        # Construct MongoDB URI
        if mongo_user and mongo_pass:
            mongo_uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}/{mongo_db}"
        else:
            mongo_uri = f"mongodb://{mongo_host}/{mongo_db}"
            
        logger.debug("Attempting to connect to MongoDB...")
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        
        # Test connection
        client.admin.command('ping')
        logger.debug("Successfully connected to MongoDB")
        return True
        
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {str(e)}")
        return False

if __name__ == "__main__":
    test_mongo_connection()