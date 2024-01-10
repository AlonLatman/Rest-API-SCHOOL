"""Basic class function with inheritance"""
class Person:
    def __init__(self, name: str, email: str, person_id: int):
        self.name = name
        self.email = email
        self.person_id = person_id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPersonId(self):
        return self.person_id


'''simple class the inherit some of the parameters from Person '''
class Student(Person):
    def __init__(self, name: str, email: str, student_id: int, gender: str, GPA: float, age: int, duration_of_studying: int, curriculum: str):
        super().__init__(name, email, student_id)
        self.age = age
        self.gender = gender
        self.GPA = GPA
        self.curriculum = curriculum
        self.duration_of_studying = duration_of_studying

'''simple class the inherit some of the parameters from Person '''
class Staff(Person):
     def __init__(self, name: str, email: str, staff_id: int, position: str, age: int, gender: str, seniority: int):
        super().__init__(name, email, staff_id)
        self.position = position
        self.age = age
        self.gender = gender
        self.seniority = seniority