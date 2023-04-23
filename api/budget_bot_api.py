from flask_app.app import create_app

if __name__ == '__main__':
    create_app = create_app()
    create_app.run(debug=True)
else:
    gunicorn_app = create_app()
