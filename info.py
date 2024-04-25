from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS
info = Flask(__name__)
CORS(info)

client=MongoClient('mongodb://localhost:27017')
db=client['data']
collection=db['info']

@info.route('/as', methods=['POST'])
def add_methods():
    new=request.get_json()
    collection.insert_one(new)
    return jsonify({"Message":"Data inserted completely"})

@info.route('/add', methods=['GET'])
def get_info():
    data=list(collection.find())
    for item in data:
        item['_id']=str(item['_id'])
    return jsonify(data)
    
if __name__ == '__main__':
    info.run(debug=True)    