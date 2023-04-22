from flask import Flask
from flask_app.controller.lineitemrest import lineitem_bp

app = Flask(__name__)
app.register_blueprint(lineitem_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
