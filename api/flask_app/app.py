from flask import Flask, request, jsonify
from flask_app.controllers.lineitemREST import lineitem_bp
from flask_app.controllers.heartbeatREST import heartbeat_bp
from flask_app.controllers.messageREST import message_bp
from flask_app import API_KEY

def create_app(config=None):
    app = Flask(__name__)

    @app.before_request
    def authenticate():
        provided_key = request.headers.get('API_KEY')
        if provided_key != API_KEY:
            response = {'message': 'Invalid API key provided'}
            return jsonify(response), 401

    # Register blueprints
    app.register_blueprint(lineitem_bp)
    app.register_blueprint(heartbeat_bp)
    app.register_blueprint(message_bp)

    return app
