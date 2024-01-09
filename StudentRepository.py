from typing import Optional
from mysql.connector import Error

class StudentRepository:
    from models import Student

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_query(self, query, params):
        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, params)
                self.db_connection.commit()
            return True
        except Error as e:
            print(f"Error: {e}")
            return False

    def execute_select_query(self, query, params):
        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Error as e:
            print(f"Error: {e}")
            return None

    def add_student(self, student: Student) -> bool:
        existing_student = self.get_student(student.person_id)
        if existing_student:
            print(f"Student with ID {student.person_id} already exists.")
            return False

        query = "INSERT INTO students (name, email, id, gender, GPA, age, duration_of_studying, curriculum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        return self.execute_query(query, (student.name, student.email, student.person_id, student.gender, student.GPA, student.age, student.duration_of_studying,
                                          student.curriculum))

    def get_student(self, student_id: int) -> Optional[Student]:
        query = "SELECT * FROM students WHERE id = %s"
        result = self.execute_select_query(query, (student_id,))
        if result is not None:
            from main import Student
            return Student(result[1], result[2], result[0], result[3], result[4], result[5], result[6], result[7])
        return None

    def update_student(self, student_id: int, updated_student: Student) -> bool:
        query = "UPDATE students SET name = %s, email = %s, GPA = %s WHERE id = %s"
        return self.execute_query(query, (updated_student.name, updated_student.email, student_id))

    def delete_student(self, student_id: int) -> bool:
        query = "DELETE FROM students WHERE id = %s"
        return self.execute_query(query, (student_id,))

    def get_random_student(self) -> object:
        query = "SELECT * FROM students ORDER BY RAND() LIMIT 1"
        result = self.execute_select_query(query)
        if result:
            from main import Student
            return Student(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        return None