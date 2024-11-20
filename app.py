from flask import Flask 
import requests
import os
from dotenv import load_dotenv, dotenv_values
from html.parser import HTMLParser
import re

app = Flask(__name__)
load_dotenv()

events = []
eventBuilder = []


class CourtReserveParser(HTMLParser):

    building = False
    parsing = False
    events = []
    eventBuilder = []

    def handle_starttag(self, tag, attrs):
        if attrs:
            for attr in attrs:
                if attr[0] == "class" and attr[1] == "details":
                    self.building = True
                    
                elif attr[0] =="class" and attr[1] == "pjlv5":
                    self.building = False
                

    def handle_data(self, data):

        if self.building:
            whitespaceFixedData = re.sub(' +', ' ', data.replace("\n", "").replace("\r", ""))
            if whitespaceFixedData != ' ':
                if whitespaceFixedData == 'TENNIS FAST FEED OWES ' or whitespaceFixedData == 'PICKLEBALL ADULT CLINICS AND FAST FEEDS ':
                    self.eventBuilder = []
                elif "remaining" in whitespaceFixedData:
                    self.eventBuilder.append(whitespaceFixedData)
                    self.events.append(self.eventBuilder)
                else: 
                    self.eventBuilder.append(whitespaceFixedData)

    def printAllData(self):
        for event in self.events:
            print(event)

parser = CourtReserveParser()


@app.route("/")
def home():
    headers = {'FilterText':'fast feed'}
    response = requests.get(os.getenv("EVENT_API_PATH"),headers)
    parser.feed(response.json()["data"])
    parser.printAllData()
    return "Hello World"

@app.route("/health")
def healthCheck():
    return "Volley is doing great!"