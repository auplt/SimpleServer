from flask import Flask
from flask import request
from flask import jsonify
import json

with open('test.json') as json_file:
    json_data = json.load(json_file)

app = Flask(__name__)


@app.route('/api/rows', methods=['GET'])
def rows_index():
    return jsonify(json_data)
