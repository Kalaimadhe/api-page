from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId

register = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db=client['register']
collection=db['student']

@register.route('/view', methods=['POST'])
def add_register():
    new = request.get_json()
    collection.insert_one(new)
    return jsonify({"message" : "Data added completely"})

@register.route('/data/<id>',methods=['PUT'])
def update_data(id):
    update_data=request.get_json()
    collection.update_one({'_id':ObjectId(id)},{'$set':update_data})
    return jsonify({"message":"value added successfully"})

@register.route('/datas/<id>',methods=['DELETE'])
def delete_register(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({"mata deleted"})

if __name__ == '__main__':
    register.run(debug=True)