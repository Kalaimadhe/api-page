from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db=client['system']
collection=db['doctor']

@app.route('/doctor/<doctor_id>/book', methods=["POST"])
def post_book(doctor_id):
    return jsonify({'message':'Appointment booked successfully'})

@app.route('/doctor', methods=['GET'])
def get_doctor():
    doctor = list(doctor.find({}, {'_id':0}))
    return jsonify(doctor)

@app.route('/doctor/<doctor_id>',methods=['GET'])
def get_doctor(doctor_id):
    doctor = doctor.find_one({'id': doctor_id},{'_id':0})
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({'error':'Doctor not found'})

@app.route('/doctor/<doctor_id>/available',methods=['GET'])
def get_check(doctor_id):
    return jsonify({'message' : 'Doctor available'})

if __name__ == "__main__":
    app.run(debug=True)