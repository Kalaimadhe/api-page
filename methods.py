from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId

methods=Flask(__name__)

client=MongoClient('mongodb://localhost:27017')
db=client['portal']
collection=db['exams']

# POST Method :
@methods.route('/a',methods=['POST'])
def add_methods():
    new=request.get_json()
    collection.insert_one(new)
    return jsonify({"message":"Data added completely"})

# GET Method :
@methods.route('/b',methods=['GET'])
def get_methods():
    data=list(collection.find())
    for item in data:
        item ['_id']=str(item['_id'])
    return jsonify(data)

# PUT Method :
@methods.route('/data/<id>',methods=['PUT'])
def update_data(id):
    update_data=request.get_json()
    collection.update_one({'_id':ObjectId(id)},{'$set':update_data})
    return jsonify({"message":"Data updated successfully"})

# DELETE Method :
@methods.route('/c/<id>',methods=['DELETE'])
def delete_data(id):
    collection.delete_one({'_id':ObjectId(id)})
    return jsonify({"message":"Data deleted completely"})

if __name__ == '__main__':
    methods.run(debug=True)
    