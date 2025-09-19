from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
students = {}

# Create - Add Student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student_id = str(len(students) + 1)
    students[student_id] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "course": data.get("course")
    }
    return jsonify({"id": student_id, "message": "Student added successfully"}), 201

# Read - Get All Students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# Read - Get Student by ID
@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
