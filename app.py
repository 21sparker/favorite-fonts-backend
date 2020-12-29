from flask import Flask
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", default="None")

@app.route('/')
def index():
    return "<h1>Welcome to our server!</h1>"

@app.route('/getdata', methods=['GET'])
def get_api_data():
    r = requests.get(f"https://www.googleapis.com/webfonts/v1/webfonts?key={API_KEY}")
    return r.json()

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
