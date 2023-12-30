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


'''even due it's initialized at person it's important to initialize it for other class as well'''
class Student(Person):
    def __init__(self, name: str, email: str, student_id: int):
        super().__init__(name, email, student_id)


class Staff(Person):
    def __init__(self, name: str, email: str, staff_id: int, position: str):
        super().__init__(name, email, staff_id)
        self.position = position