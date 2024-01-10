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

    """
    This test case validates the student reading functionality of the application's route handling.

    The test performs the following steps:
    1. Generates a random student ID within a specified range.
    2. Attempts to retrieve a student with the generated ID via a GET request to '/students/{id}'.
       Since the student does not exist yet, a 404 status code (Not Found) is expected.
    3. Creates a new student with the random ID and some predefined attributes 
       (name, email, gender, GPA, age, grade, and major) and adds it to the student repository.
    4. Attempts again to retrieve the same student. This time, since the student exists,
       a 200 status code (OK) is expected.
    5. Finally, the newly added student is removed from the repository to clean up.

    Assertions:
    - Asserts that the response status code is 404 (Not Found) when trying to access a non-existent student.
    - Asserts that the response status code is 200 (OK) when the student is successfully retrieved.

    Note:
    - The Student object creation and addition to the repository are part of the test setup and not part of the actual application's student retrieval functionality.
    - The test assumes the presence of a Student class and a student repository (`Student_repo`) for creating and handling student objects.
    - The 'app' attribute of 'self' should be an instance of the application or a test client associated with the application.
    """
    def test_read_student_route(self):
        random_id = random.randint(1000, 9999)

        response = self.app.get('/students/{}'.format(random_id))
        self.assertEqual(response.status_code, 404)

        new_student = Student("Test Student", "test@example.com", random_id, "Male", 5.3, 36, 4,"CS")
        self.Student_repo.add_student(new_student)

        response = self.app.get(f'/students/{random_id}')
        self.assertEqual(response.status_code, 200)

        self.Student_repo.delete_student(random_id)

    """
    This test case validates the staff reading functionality of the application's route handling.

    The test performs the following steps:
    1. Generates a random staff ID within a specified range.
    2. Attempts to retrieve a staff member with the generated ID via a GET request to '/staff/{id}'.
       Since the staff member does not exist yet, a 404 status code (Not Found) is expected.
    3. Creates a new staff member with the random ID and some predefined attributes 
       (name, email, age, gender, experience) and adds it to the staff repository.
    4. Attempts again to retrieve the same staff member. This time, since the staff member exists,
       a 200 status code (OK) is expected.
    5. Finally, the newly added staff member is removed from the repository to clean up.

    Assertions:
    - Asserts that the response status code is 404 (Not Found) when trying to access a non-existent staff member.
    - Asserts that the response status code is 200 (OK) when the staff member is successfully retrieved.

    Note:
    - The Staff object creation and addition to the repository are part of the test setup and not part of the actual application's staff retrieval functionality.
    - The test assumes the presence of a Staff class and a staff repository (`Staff_repo`) for creating and handling staff objects.
    - The 'app' attribute of 'self' should be an instance of the application or a test client associated with the application.
    """
    def test_read_staff_route(self):
        random_id = random.randint(1000, 9999)

        response = self.app.get('/staff/{}'.format(random_id))
        self.assertEqual(response.status_code, 404)

        new_staff = Staff("Test Staff", "test@example.com", random_id, "Teacher", 38, "Female", 15)
        self.Staff_repo.add_staff(new_staff)

        response = self.app.get(f'/staff/{random_id}')
        self.assertEqual(response.status_code, 200)

        self.Staff_repo.delete_staff(random_id)

    """
    This test case assesses the ability to add multiple random students to the repository and then calculate some basic statistics.

    The test performs the following steps:
    1. Defines a set of curriculums.
    2. Initializes an empty list to keep track of added students.
    3. Adds 10 random students to the student repository. Each student is generated with random attributes, including a unique student ID, gender, GPA, age, duration of studying, and chosen curriculum.
    4. Initializes a dictionary to count the number of students in each curriculum and a variable to track the total duration of studying for all students.
    5. Iterates over the added students to update the curriculum counts and calculate the total duration of studying.
    6. Calculates the average duration of studying based on the total duration and the number of students.
    7. Outputs the average duration of study and the counts of students in each curriculum.
    8. Removes all the added students from the repository to clean up.

    Assertions:
    - There are no explicit assertions in this test, but it serves to demonstrate the functionality of adding students, performing calculations, and cleaning up.

    Note:
    - The test assumes the presence of a Student class and a student repository (`Student_repo`) for creating and handling student objects.
    - The test uses random generation for student attributes, which means the output (average duration and curriculum counts) will vary each time the test is run.
    - The 'print' statements are used for demonstration and could be replaced with assertions in a more rigorous test scenario.
    """
    def test_add_random_students_and_statistics(self):
        curriculums = ["CS", "Math", "Law"]
        students_added = []

        # Add 10 random students
        for _ in range(10):
            student = Student(
                name=f"Student {_}",
                email=f"student{_}@example.com",
                student_id=random.randint(10000, 99999),
                gender="Male" if random.randint(0, 1) else "Female",
                GPA=random.uniform(2.0, 4.0),
                age=random.randint(20, 35),
                duration_of_studying=random.randint(1, 4),
                curriculum=random.choice(curriculums)
            )
            self.Student_repo.add_student(student)
            students_added.append(student)

        curriculum_counts = {curriculum: 0 for curriculum in curriculums}
        total_duration = 0

        for student in students_added:
            curriculum_counts[student.curriculum] += 1
            total_duration += student.duration_of_studying

        average_duration = total_duration / len(students_added)

        print("Average Duration of Study:", average_duration)
        print("Curriculum Counts:", curriculum_counts)

        for student in students_added:
            self.Student_repo.delete_student(student.person_id)

    """
    This test case evaluates the addition of multiple random staff members to the repository and then calculates various statistics.

    The test performs the following steps:
    1. Defines a set of genders and staff positions.
    2. Initializes an empty list to track the staff members added.
    3. Adds 10 random staff members to the staff repository. Each staff member is generated with random attributes, including a unique staff ID, position, gender, age, and seniority.
    4. Calculates the total and average age of all the added staff members.
    5. Initializes a dictionary to count the number of staff members in each position and another dictionary to track the distribution of their seniority.
    6. Updates the counts and distribution based on the attributes of each added staff member.
    7. Outputs the average age, position counts, and seniority distribution.
    8. Removes all the added staff members from the repository to clean up.

    Assertions:
    - Like the student test case, there are no explicit assertions in this test. It is designed to demonstrate the functionality of adding staff, performing calculations, and cleaning up.

    Note:
    - The test assumes the presence of a Staff class and a staff repository (`Staff_repo`) for creating and handling staff objects.
    - The test uses random generation for staff attributes, which means the output (average age, position counts, and seniority distribution) will vary each time the test is run.
    - The 'print' statements are used for demonstration purposes and could be replaced with assertions in a more comprehensive testing scenario.
    """
    def test_add_random_staff_and_statistics(self):
        genders = ["Male", "Female"]
        staff_added = []
        positions = ["CS lecturer", "Math lecturer", "Head of Math department", "Head of CS department"]

        # Add 10 random staff members
        for _ in range(10):
            staff = Staff(
                name=f"Staff {_}",
                email=f"staff{_}@example.com",
                staff_id=random.randint(10000, 99999),
                position=random.choice(positions),
                gender=random.choice(genders),
                age=random.randint(35, 75),
                seniority=random.randint(1, 20)  # Assuming seniority is in years
            )
            self.Staff_repo.add_staff(staff)
            staff_added.append(staff)

        total_age = sum(staff.age for staff in staff_added)
        average_age = total_age / len(staff_added)

        positions_count = {position: 0 for position in positions}

        seniority_distribution = {}
        for staff in staff_added:
            seniority_distribution[staff.seniority] = seniority_distribution.get(staff.seniority, 0) + 1
            positions_count[staff.position] += 1

        print("Average Age:", average_age)
        print("position count: ", positions_count)
        print("Seniority Distribution:", seniority_distribution)

        for staff in staff_added:
            self.Staff_repo.delete_staff(staff.person_id)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()