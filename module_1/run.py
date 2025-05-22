from flask import Flask
from pages.routes import pages_bp

app = Flask(__name__)
app.register_blueprint(pages_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 
