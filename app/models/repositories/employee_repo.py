from sqlalchemy.orm import Session
from ..models import Employee
from app.interfaces.data_access import IEmployeeRepository


class EmployeeRepository(IEmployeeRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_employee(self, employee: dict):
        try:
            employee_to_add = Employee(**employee)
            self.db.add(employee_to_add)
            self.db.commit()
            self.db.refresh(employee_to_add)
            return employee_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding Employee: {e}")
            raise

    def get_all_employees(self):
        return self.db.query(Employee).all()

    def get_employee_by_id(self, employee_id: int):
        return self.db.query(Employee).filter_by(id=employee_id).first()

    def edit_employee(self, employee_id: int, new_data: dict):
        employee = self.get_employee_by_id(employee_id)
        employee.name = new_data['name']
        employee.contacts = new_data['contacts']
        employee.department = new_data['department']
        self.db.commit()

    def delete_employee(self, employee_id: int):
        employee = self.get_employee_by_id(employee_id)
        self.db.delete(employee)
        self.db.commit()
