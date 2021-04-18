from flask import Flask, request, jsonify
from resources.routes import controller

app = Flask(__name__)
app.register_blueprint(controller)
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(port = 5000, debug=True)