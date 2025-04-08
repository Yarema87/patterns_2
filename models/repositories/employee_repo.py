from sqlalchemy.orm import Session
from ..models import Employee
from interfaces.data_access import IEmployeeRepository


class EmployeeRepository(IEmployeeRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_employee(self, employee: Employee):
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)

    def get_all_employees(self):
        return self.db.query(Employee).all()

    def get_employee_by_id(self, employee_id: int):
        return self.db.query(Employee).filter_by(id=employee_id).first()