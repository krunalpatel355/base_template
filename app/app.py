import logging
from flask import Flask, jsonify

logger = logging.getLogger(__name__)

def create_app():
    logger.debug("Initializing Flask application")
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({"status": "ok", "message": "Flask app is running"})
    
    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"})
    
    logger.debug("Flask application initialized successfully")
    return app