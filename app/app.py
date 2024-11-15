# app/app.py
from flask import Flask, jsonify
from app.utils.mongo_utils import init_mongo

def create_app():
    app = Flask(__name__)
    
    try:
        app.db = init_mongo()
    except Exception as e:
        app.logger.error(f"Failed to initialize MongoDB: {e}")
        app.db = None

    @app.route('/health')
    def health_check():
        health_status = {
            'status': 'healthy',
            'mongodb_connected': app.db is not None
        }
        return jsonify(health_status)

    return app