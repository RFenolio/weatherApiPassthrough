from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

DARK_URL = 'https://api.darksky.net/forecast/%s/%s,%s?exclude=[daily,hourly,minutely,alerts,flags]'
OPEN_URL = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s'
DARK_API_KEY = os.environ.get('DARK_API_KEY')
OPEN_API_KEY = os.environ.get('OPEN_API_KEY')

@app.route('/')
def root():
    return "Hi, this is my site to redirect weather API calls so I can deploy on codepen"

@app.route('/dark')
def get_dark_weather():
    """
    This route queries darksky.net's weather service
    It passes the result directly as the response
    """
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    r = requests.get(DARK_URL %(DARK_API_KEY, lat, lon))
    return jsonify(r.json())

@app.route('/open')
def get_open_weather():
    """
    This route queries openweathermap.org's weather service
    It passes the result directly as the response
    """
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    r = requests.get(OPEN_URL %(lat, lon, OPEN_API_KEY))
    return jsonify(r.json())