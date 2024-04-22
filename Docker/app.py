from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://nosql-db:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/', methods=['GET'])
def get_values():
    return str(list(collection.find()))

@app.route('/', methods=['POST'])
def create_value():
    key = request.form['key']
    value = request.form['value']
    collection.insert_one({'key': key, 'value': value})
    return 'Value created'

@app.route('/', methods=['PUT'])
def update_value():
    key = request.form['key']
    new_value = request.form['new_value']
    collection.update_one({'key': key}, {'$set': {'value': new_value}})
    return 'Value updated'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)