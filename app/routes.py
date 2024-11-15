from flask import jsonify, request
from app.app import app

@app.route('/')
def home():
    return jsonify({
        "message": "Hello, World!"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        "received": data
    })