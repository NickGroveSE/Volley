from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")
@cross_origin(supports_credentials=True)
def home():
    return jsonify({"Success": "Hello World, I am Volley! Lousiville Indoor Racquet Club's Admin Control."})


# Deployment Error Lets Try Again
@app.route("/credentials_check")
@cross_origin(supports_credentials=True)
def credential_check():
    auth_header = request.headers.get('Authorization')

    if auth_header:
        return jsonify({"Authorized": auth_header})
    else:
        return jsonify({"Unauthorized": "401"})
    