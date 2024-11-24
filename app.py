from flask import Flask 
import requests
import os
from dotenv import load_dotenv, dotenv_values
from html.parser import HTMLParser
import re

app = Flask(__name__)
load_dotenv()


@app.route("/")
def home():
    return "Hello World, I am Volley! Lousiville Indoor Racquet Club's Admin Control."

@app.route("/health")
def healthCheck():
    return "Volley is doing great!"

@app.route("/auth_modal")
def auth_model():
    return "Auth Modal Incoming"

@app.route("/credentials")
def credential_check():
    return "Checking Credentials"