import mysql.connector
from mysql.connector import Error
from main import Staff, Student

class SchoolDatabase:
    def __init__(self):
        self.connection = self.create_connection()

    @staticmethod
    def create_connection():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='mydatabase',
                user='root',
                password='')
            return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def execute_query(self, query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
            return True
        except Error as e:
            print(f"Error: {e}")
            return False

    def execute_select_query(self, query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Error as e:
            print(f"Error: {e}")
            return None

    def add_student(self, student: Student) -> bool:
        query = "INSERT INTO students (name, email, id) VALUES (%s, %s, %s)"
        return self.execute_query(query, (student.name, student.email, student.ID))

    def get_student(self, student_id: int) -> Student:
        query = "SELECT * FROM students WHERE id = %s"
        result = self.execute_select_query(query, (student_id,))
        if result:
            return Student(result['name'], result['email'], result['id'])
        return None

    def update_student(self, student_id: int, updated_student: Student) -> bool:
        query = "UPDATE students SET name = %s, email = %s WHERE id = %s"
        return self.execute_query(query, (updated_student.name, updated_student.email, student_id))

    def delete_student(self, student_id: int) -> bool:
        query = "DELETE FROM students WHERE id = %s"
        return self.execute_query(query, (student_id,))

    def add_staff(self, staff: Staff) -> bool:
        query = "INSERT INTO staff (name, email, id, position) VALUES (%s, %s, %s, %s)"
        return self.execute_query(query, (staff.name, staff.email, staff.ID, staff.position))

    def get_staff(self, staff_id: int) -> Staff:
        query = "SELECT * FROM staff WHERE id = %s"
        result = self.execute_select_query(query, (staff_id,))
        if result:
            return Staff(result['name'], result['email'], result['id'], result['position'])
        return None

    def update_staff(self, staff_id: int, updated_staff: Staff) -> bool:
        query = "UPDATE staff SET name = %s, email = %s, position = %s WHERE id = %s"
        return self.execute_query(query, (updated_staff.name, updated_staff.email, updated_staff.position, staff_id))

    def delete_staff(self, staff_id: int) -> bool:
        query = "DELETE FROM staff WHERE id = %s"
        return self.execute_query(query, (staff_id,))

    def close_connection(self):
        if self.connection:
            self.connection.close()
