from flask import Flask
from flask_app.controllers.lineitemREST import lineitem_bp
from flask_app.controllers.heartbeatREST import heartbeat_bp


def create_app(config=None):
    app = Flask(__name__)

    # Configure app as needed
    if config:
        app.config.from_object(config)

    # Register blueprints
    app.register_blueprint(lineitem_bp)
    app.register_blueprint(heartbeat_bp)

    return app
