from typing import Optional
from mysql.connector import Error

class StaffRepository:
    from models import Staff

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

    def add_staff(self, staff: Staff) -> bool:
        query = "INSERT INTO staff (name, email, id, position) VALUES (%s, %s, %s, %s)"
        return self.execute_query(query, (staff.name, staff.email, staff.person_id, staff.position))

    def get_staff(self, staff_id: int) -> Optional[Staff]:
        query = "SELECT * FROM staff WHERE id = %s"
        result = self.execute_select_query(query, (staff_id,))
        if result is not None:
            from main import Staff
            return Staff(result[1], result[2], result[0], result[3])
        return None

    def update_staff(self, staff_id: int, updated_staff: Staff) -> bool:
        query = "UPDATE staff SET name = %s, email = %s, position = %s WHERE id = %s"
        return self.execute_query(query, (updated_staff.name, updated_staff.email, updated_staff.position, staff_id))

    def delete_staff(self, staff_id: int) -> bool:
        query = "DELETE FROM staff WHERE id = %s"
        return self.execute_query(query, (staff_id,))
