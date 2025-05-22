from flask import Flask
from pages.routes import pages_bp

def create_app():
    """
    Creates the application and registers the blueprints.
    """
    app = Flask(__name__)
    app.register_blueprint(pages_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000) 
