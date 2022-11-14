from flask import Flask
from flask import request
from flask import jsonify
rows_base = [
{'id': 1, 'info':'Тест 1'},
{'id': 2, 'info':'Тест 2'},
{'id': 3, 'info':'Тест 3'},
{'id': 4, 'info':'Тест 4'},
{'id': 5, 'info':'Тест 5'} ]
rows_id_seq = 6


app = Flask(__name__)

@app.route('/api/rows', methods=['GET'])
def rows_index():
    return jsonify(rows_base)

