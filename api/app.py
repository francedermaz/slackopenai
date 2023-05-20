from flask import Flask
from flask_cors import CORS
from routes import data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def page_not_found(error):
    return "Error"

if __name__ == '__main__':
    app.register_blueprint(data.main)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, host='0.0.0.0')
