from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from resources.routes import controller

app = Flask(__name__)
CORS(app)
app.register_blueprint(controller)
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(port = 5000, debug=True)