from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "RGAPI-518987d4-c27e-4127-941e-735c82ee4093"
API_URL = "http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion.json"

params = {
    'api_key': API_KEY
}


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
