import unittest
import random
from StaffRepository import StaffRepository
from StudentRepository import StudentRepository
from main import app, db_connection
from models import Student, Staff


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.Student_repo = StudentRepository(db_connection)
        self.Staff_repo = StaffRepository(db_connection)

    def test_read_student_route(self):
        random_id = random.randint(1000, 9999)

        response = self.app.get('/students/{}'.format(random_id))
        self.assertEqual(response.status_code, 404)

        new_student = Student("Test Student", "test@example.com", random_id)
        self.Student_repo.add_student(new_student)

        response = self.app.get(f'/students/{random_id}')
        self.assertEqual(response.status_code, 200)

        self.Student_repo.delete_student(random_id)

    def test_read_staff_route(self):
        random_id = random.randint(1000, 9999)

        response = self.app.get('/staff/{}'.format(random_id))
        self.assertEqual(response.status_code, 404)

        new_staff = Staff("Test Staff", "test@example.com", random_id, "Teacher")
        self.Staff_repo.add_staff(new_staff)

        response = self.app.get(f'/staff/{random_id}')
        self.assertEqual(response.status_code, 200)

        self.Staff_repo.delete_staff(random_id)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()