import unittest
from main import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_read_student_route(self):
        # Test the /students
        response = self.app.get('/students/1')
        print("read student response ", response.data)
        self.assertEqual(response.status_code, 200)

    def test_read_staff_route(self):
        response = self.app.get('/staff/4')
        print("read staff response ", response.data)
        self.assertEqual(response.status_code, 200)

    def test_update_student_route(self):
        student = {
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
        response = self.app.put('/students/123', json=student)
        print("update student response ", response.data)
        self.assertEqual(response.status_code, 200)

    def test_update_staff_route(self):
        staff = {
            "name": "Marie jane",
            "email": "marie@example.com",
            "position": "Doctor"
        }
        response = self.app.put('/staff/3', json=staff)
        print("update staff response ", response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_student_route(self):
        response = self.app.delete('/students/123')
        print("delete student response ", response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_staff_route(self):
        response = self.app.delete('/staff/3')
        print("delete staff response ", response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()