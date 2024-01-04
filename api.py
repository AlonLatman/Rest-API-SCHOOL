from StaffRepository import StaffRepository
from StudentRepository import StudentRepository
from models import Staff, Student

class SchoolAPI:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_student_endpoint(self, request_data):
        name = request_data.get("name")
        email = request_data.get("email")
        student_Id = request_data.get("id")

        if not all(name, email, student_Id):
            return {"error": "Missing data"}, 400

        new_Student = Student(name, email, student_Id)
        student_repo = StudentRepository(self.db_connection)
        success = student_repo.add_student(new_Student)

        if success:
            return {"message": "Student added successfully"}, 201
        else:
            return {"error": "Failed to add student"}, 500

    def read_student_endpoint(self, student_id):
        student_repo = StudentRepository(self.db_connection)
        student = student_repo.get_student(student_id)
        if student is not None:
            return {"student": student.__dict__}, 200
        else:
            return {"error": "Student not found"}, 404

    def update_student_endpoint(self, student_id, request_data):
        name = request_data.get("name")
        email = request_data.get("email")

        updated_student = Student(name, email, student_id)
        student_repo = StudentRepository(self.db_connection)
        success = student_repo.update_student(student_id, updated_student)

        if success:
            return {"message": "Student updated successfully"}, 200
        else:
            return {"error": "Failed to update student"}, 500

    def delete_student_endpoint(self, student_id):
        student_repo = StudentRepository(self.db_connection)
        success = student_repo.delete_student(student_id)

        if success:
            return {"message": "Student deleted successfully"}, 200
        else:
            return {"error": "Failed to delete student"}, 500

    def create_staff_endpoint(self, request_data):
        name = request_data.get("name")
        email = request_data.get("email")
        staff_Id = request_data.get("id")
        staff_Position = request_data.get("position")

        if not all(name, email, staff_Id, staff_Position):
            return {"error": "Missing data"}, 400

        new_Staff = Staff(name, email, staff_Id, staff_Position)
        staff_repo = StaffRepository(self.db_connection)
        success = staff_repo.add_staff(new_Staff)

        if success:
            return {"message": "staff added successfully"}, 201
        else:
            return {"error": "Failed to add staff"}, 500

    def read_staff_endpoint(self, staff_id):
        staff_repo = StaffRepository(self.db_connection)
        staff = staff_repo.get_staff(staff_id)

        if staff is not None:
            return {"staff": staff.__dict__}, 200
        else:
            return {"error": "Staff not found"}, 404

    def update_staff_endpoint(self, staff_id, request_data):
        name = request_data.get("name")
        email = request_data.get("email")
        position = request_data.get("position")

        updated_staff = Staff(name, email, staff_id, position)
        staff_repo = StaffRepository(self.db_connection)
        success = staff_repo.update_staff(staff_id, updated_staff)

        if success:
            return {"message": "Staff updated successfully"}, 200
        else:
            return {"error": "Failed to update staff"}, 500

    def delete_staff_endpoint(self, staff_id):
        staff_repo = StaffRepository(self.db_connection)
        success = staff_repo.delete_staff(staff_id)

        if success:
            return {"message": "Staff deleted successfully"}, 200
        else:
            return {"error": "Failed to delete staff"}, 500

    @staticmethod
    def get_random_student():
        student = StudentRepository.get_random_student()
        if student:
            return student.to_dict()
        else:
            return {"error": "No students available"}