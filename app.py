from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests
import os
from dotenv import load_dotenv, dotenv_values
from html.parser import HTMLParser
import re

app = Flask(__name__)
CORS(app, support_credentials=True)
load_dotenv()


@app.route("/")
@cross_origin(supports_credentials=True)
def home():
    return jsonify({"Success": "Hello World, I am Volley! Lousiville Indoor Racquet Club's Admin Control."})


# Deployment Error Lets Try Again
@app.route("/credentials_check")
@cross_origin(supports_credentials=True)
def credential_check(request):
    auth_header = request.headers.get('Authorization')

    if auth_header:
        return jsonify({"Authorized": auth_header})
    else:
        return 'Unauthorized', 401
    