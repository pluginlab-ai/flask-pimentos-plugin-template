from flask import Flask, jsonify
import random
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Pimento! Ask ChatGPT for the pimento of the day.'

@app.route('/logo.jpg')
def flask_logo():
    return app.send_static_file('logo.jpg')

@app.route('/pimento_of_the_day')
def pimento_of_the_day():
    current_path = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_path, '..', 'data', 'pimentos.json')

    with open(json_file_path) as f:
        pimentos = json.load(f)
    random_pimento = random.choice(pimentos)
    return jsonify(random_pimento)
