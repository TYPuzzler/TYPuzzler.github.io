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

# http://typuzzler.pythonanywhere.com/meta/"nameOfPuzzle"
# Returns a JSON dictionary of metadata of the specified puzzle.
#   {"1":["url1", "rarity1", x1, y1],
#    "2":["url2", "rarity2", x2, y2],
#    ...}
@app.route('/meta/<string:nameOfPuzzle>', methods=['GET'])
def meta(nameOfPuzzle):
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

# http://typuzzler.pythonanywhere.com/piece/"nameOfPuzzle"/"num"
# Returns a JSON string of the metadata of the specified piece.
#   ["url", x, y]
@app.route('/piece/<string:nameOfPuzzle>/<string:num>', methods=['GET'])
def piece(nameOfPuzzle, num):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    n = str(json.loads(num))
    query = 'SELECT url, x, y FROM ' + name + ' where piece_num = ' + n
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result[0])

# http://typuzzler.pythonanywhere.com/full/"nameOfPuzzle"
# Returns a JSON string of the metadata of the specified full puzzle.
#   ["url", x, y]
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

# http://typuzzler.pythonanywhere.com/gray/"nameOfPuzzle"
# Returns a JSON string of the metadata of the grayscale version of the specified
# full puzzle.
#   ["url", x, y]
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

# http://typuzzler.pythonanywhere.com/random/"nameOfPuzzle"
# Returns a JSON string of the metadata of a random piece in the specified puzzle.
#   [num, "url", "rarity", x, y]
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

    query = 'SELECT piece_num, url, rarity, x, y FROM ' + name + ' where rarity="' + rarity + '" ORDER BY RAND() LIMIT 1'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result[0])

# http://typuzzler.pythonanywhere.com/random/"nameOfPuzzle"/"acc"/"spd"
# Returns a JSON string of the metadata of a random piece in the specified puzzle
# based on user statistics.
#   [num, "url", "rarity", x, y]
@app.route('/random/<string:nameOfPuzzle>/<string:acc>/<string:spd>', methods=['GET'])
def random_piece_test(nameOfPuzzle, acc, spd):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    acc = float(str(json.loads(acc)))
    spd = float(str(json.loads(spd)))
    setting = [0.55, 0.8, 0.95]
    if acc > 0.95 and spd > 100:
        setting[0] = 0.3
        setting[1] = 0.45
        setting[2] = 0.6
    elif acc > 0.95 and spd > 80:
        setting[0] = 0.3
        setting[1] = 0.5
        setting[2] = 0.8

    n = random.random()

    rarity = ''
    if n < setting[0]:
        rarity = 'N'
    elif n < setting[1]:
        rarity = 'R'
    elif n < setting[2]:
        rarity = 'SR'
    else:
        rarity = 'SSR'

    query = 'SELECT piece_num, url, rarity, x, y FROM ' + name + ' where rarity="' + rarity + '" ORDER BY RAND() LIMIT 1'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result[0])

# http://typuzzler.pythonanywhere.com/trans/"nameOfPuzzle"/
# Returns a JSON string of a metadata dictionary of a set of semi-transparent
# versions of the pieces in the specified puzzle.
#   {"1":["url1", x1, y1],
#    "2":["url2", x2, y2],
#    ...}
@app.route('/trans/<string:nameOfPuzzle>', methods=['GET'])
def trans_piece(nameOfPuzzle):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    query = 'SELECT piece_num, trans_url, x, y FROM ' + name
    cursor.execute(query)
    dic = {}
    for num, url, x, y in cursor:
        dic[num] = (url, x, y)
    cursor.close()
    cnx.close()
    return jsonify(dic)
