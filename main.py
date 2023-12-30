from flask import Flask, request, jsonify
from api import SchoolAPI
import mysql.connector
import logging
from models import Student, Staff

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='963741Aa@',
    database='mydatabase'
)

school_api = SchoolAPI(db_connection)

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "This is a test response"}), 200

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    response = school_api.create_student_endpoint(data)
    return jsonify(response)
@app.route('/students/<int:student_id>', methods=['GET'])
def read_student(student_id):
    return jsonify(school_api.read_student_endpoint(student_id))

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    return jsonify(school_api.update_student_endpoint(student_id, data))

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    return jsonify(school_api.delete_student_endpoint(student_id))

@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.json
    return jsonify(school_api.create_staff_endpoint(data))

@app.route('/staff/<int:staff_id>', methods=['GET'])
def read_staff(staff_id):
    return jsonify(school_api.read_staff_endpoint(staff_id))

@app.route('/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    data = request.json
    return jsonify(school_api.update_staff_endpoint(staff_id, data))

@app.route('/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    return jsonify(school_api.delete_staff_endpoint(staff_id))

if __name__ == '__main__':
    app.run(debug=True)
