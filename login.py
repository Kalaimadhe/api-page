from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId

login = Flask(__name__)

client=MongoClient('mongodb://localhost:27017')
db=client['id']
collection=client['mailid']

@login.route('/db', methods=['POST'])
def add_login():
    data = request.get_json()
    mailid = data.get('mailid')
    password = data.get('password')
    
    if not mailid or not password:
        return jsonify({"Error":"Email id and password are required"})
    
    if collection.mailid.find_one({"mailid":mailid}):
        return jsonify({"Error":"Email id already exists"})
    
    if collection.mailid.insert_one({"mailid":mailid, "password":password}):
        return jsonify({"message":"User registered successfully"})
       
if __name__ == '__main__':
    login.run(debug=True)