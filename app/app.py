from flask import Flask
from app.config import Config
from app.utils.mongo_utils import init_mongo
from app.routes.main_routes import register_routes

def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(Config())
    
    # Initialize MongoDB
    init_mongo(app)
    
    # Register routes
    register_routes(app)
    
    return app