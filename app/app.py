from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

stuff = {'theFirst': 1,
            'theSecond': 2}

DARK_URL = 'https://api.darksky.net/forecast/%s/%s,%s?exclude=[daily,hourly,minutely,alerts,flags]'
OPEN_URL = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s'
LAT = '40.7128'
LONG = '-74.0059'


@app.route('/')
def root():
    return "Hi, this is my site to redirect weather API calls so I can deploy on codepen"

@app.route('/dark')
def get_dark_weather():
    lat = request.args.get('lat', LAT)
    lon = request.args.get('lon', LONG)
    r = requests.get(DARK_URL %(os.environ.get('DARK_API_KEY'), lat, lon))
    return r.json()

@app.route('/open')
def get_open_weather(lat, long):
    lat = request.args.get('lat', LAT)
    lon = request.args.get('lon', LONG)
    r = requests.get(OPEN_URL %(lat, lon, os.environ.get('OPEN_API_KEY')))
    return r.json()