from flask import jsonify, render_template
from app.utils.mongo_utils import mongo

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/health')
    def health_check():
        try:
            mongo.db.command('ping')
            return jsonify({"status": "healthy", "mongodb": "connected"})
        except Exception as e:
            return jsonify({"status": "unhealthy", "error": str(e)}), 500