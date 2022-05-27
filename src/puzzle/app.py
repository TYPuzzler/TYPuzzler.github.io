import json
import random
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

config = {
    'user': 'TYPuzzler',
    'password': 'synHow-haphi2-wipqup',
    'host': 'TYPuzzler.mysql.pythonanywhere-services.com',
    'database': 'TYPuzzler$typuzzler',
    'raise_on_warnings': True
}

@app.route('/')
def index():
    return 'This is the backend server for TYPuzzler created by Bowen Tian.'

@app.route('/test/<string:nameOfPuzzle>', methods=['GET'])
def test(nameOfPuzzle):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    query = 'SELECT piece_num, url, rarity, x, y FROM ' + name
    cursor.execute(query)
    dic = {}
    for num, url, rarity, x, y in cursor:
        dic[num] = (url, rarity, x, y)

    cursor.close()
    cnx.close()
    return jsonify(dic)

@app.route('/full/<string:nameOfPuzzle>', methods=['GET'])
def get_full_puzzle(nameOfPuzzle):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    query = 'SELECT puzzle_url, x, y FROM puzzles where puzzle_name="' + name + '"'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result[0])

@app.route('/gray/<string:nameOfPuzzle>', methods=['GET'])
def get_gray_puzzle(nameOfPuzzle):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    query = 'SELECT gray_url, x, y FROM puzzles where puzzle_name="' + name + '"'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result[0])

@app.route('/random/<string:nameOfPuzzle>', methods=['GET'])
def random_piece(nameOfPuzzle):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    n = random.random()
    rarity = ''
    if n < 0.55:
        rarity = 'N'
    elif n < 0.8:
        rarity = 'R'
    elif n < 0.95:
        rarity = 'SR'
    else:
        rarity = 'SSR'

    query = 'SELECT url, rarity, x, y FROM ' + name + ' where rarity="' + rarity + '" ORDER BY RAND() LIMIT 1'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result[0])
