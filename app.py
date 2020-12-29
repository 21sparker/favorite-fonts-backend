from flask import Flask
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", default="None")

@app.route('/')
def get_api_data():
    r = requests.get(f"https://www.googleapis.com/webfonts/v1/webfonts?key={API_KEY}")
    return r.json()