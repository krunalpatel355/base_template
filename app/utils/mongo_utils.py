from flask_pymongo import PyMongo
from pymongo.errors import ConnectionError

mongo = PyMongo()

def init_mongo(app):
    mongo.init_app(app)
    try:
        # Verify connection
        mongo.db.command('ping')
        app.logger.info("MongoDB connected successfully!")
    except ConnectionError as e:
        app.logger.error(f"MongoDB connection failed: {str(e)}")
        raise