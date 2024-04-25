from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId

get = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db=client['exam']
collection=db['portal']

@get.route('/vv',methods=['POST'])
def add_get():
    new=request.get_json()
    collection.insert_one(new)
    return jsonify({"message":"Data should be done"})

@get.route('/v',methods=['GET'])
def get_items():
    data=list(collection.find())
    for item in data:
        item ['_id']=str(item['_id'])
    return jsonify(data)

if __name__=='__main__':
    get.run(debug=True)
            
