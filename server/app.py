from flask import Flask, jsonify
from flask_cors import CORS

# CORS (Cross Origin Resource Sharing) is needed to make cross-origin requests
# in production environment, only allow cross origin requests from trusted domains 

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()