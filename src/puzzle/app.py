import json
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/test/<string:nameOfPuzzle>', methods=['GET', 'POST'])
def test(nameOfPuzzle):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    name = json.loads(nameOfPuzzle)
    query = 'SELECT piece_num, url, rarity, x, y FROM ' + name
    cursor.execute(query)
    dict = {}
    for num, url, rarity, x, y in cursor:
        dict[num] = (url, rarity, x, y)
    return jsonify(dict)

# @app.route('/test')
# def test():
#     cnx = mysql.connector.connect(**config)
#     cursor = cnx.cursor()
#     name = 'JS_logo'
#     query = 'SELECT piece_num, url, rarity, x, y FROM ' + name
#     cursor.execute(query)
#     dict = {}
#     for num, url, rarity, x, y in cursor:
#         dict[num] = (url, rarity, x, y)
#         # print(num + '\n')
#     return jsonify(dict)
