from flask import Flask
from flask_app.controller.lineitemrest import lineitem_bp

def create_app(config=None):
    app = Flask(__name__)

    # Configure app as needed
    if config:
        app.config.from_object(config)

    # Register blueprints
    app.register_blueprint(lineitem_bp)

    return app