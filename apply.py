from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

get = Flask(__name__)
CORS(get)

client = MongoClient('mongodb://localhost:27017')
db=client['log']
collection=db['user']

@get.route('/var',methods=['POST'])
def add_get():
    new=request.get_json()
    collection.insert_one(new)
    return jsonify({"message":"Data should be done"})

@get.route('/var',methods=['GET'])
def get_items():
    data=list(collection.find())
    for item in data:
        item ['_id']=str(item['_id'])
    return jsonify(data)

if __name__=='__main__':
    get.run(debug=True)