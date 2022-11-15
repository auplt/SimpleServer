from flask import Flask
from flask import request
from flask import jsonify
import json


with open('test.json') as json_file:
    json_data = json.load(json_file)

app = Flask(__name__)


@app.route('/api/rows', methods=['GET'])
def rows_show():
    row_id = int(request.args.get('id'))
    data = [x for x in json_data if x["id"] == row_id]
    return jsonify(data)

# @app.route('/api/rows', methods=['GET'])
# def rows_index():
#     return jsonify(json_data)
