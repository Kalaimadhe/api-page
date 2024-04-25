from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId

log = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db=client['admin']
collection=client['info']

@log.route('/sum', methods=['POST'])
def add_log():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify ({"Error":"Email-Id and password required"})
    
    if collection.email.find_one({"email":email}):
        return jsonify ({"Error":"Email-Id already exist"})
    
    if collection.email.find_one({"email":email,"password":password}):
        return jsonify ({"Error":"User registered"})
    
if __name__ == '__main__':
    log.run(debug=True)