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
    lat = request.args.get('lat', LAT)
    long = request.args.get('long', LONG)
    service = request.args.get('service', 'dark')
    if service == 'dark':
        return jsonify(get_dark_weather(lat, long))
    elif service == 'open':
        return jsonify(get_open_weather(lat, long))
    else:
        return "did you make a mistake?"



def get_dark_weather(lat, long):
    r = requests.get(DARK_URL %(os.environ.get('DARK_API_KEY'), lat, long))
    return r.json()

def get_open_weather(lat, long):
    r = requests.get(OPEN_URL %(lat, long, os.environ.get('OPEN_API_KEY')))
    return r.json()