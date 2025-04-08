from interfaces.data_access import IEmployeeRepository
from interfaces.services import IEmployeeService
from models.models import Employee


class EmployeeService(IEmployeeService):
    def __init__(self, employee_repo: IEmployeeRepository):
        self.employee_repo = employee_repo

    def create_employee(self, employee: Employee):
        self.employee_repo.add_employee(employee)

    def employees_list(self):
        return self.employee_repo.get_all_employees()

    def get_single_employee(self, employee_id: int):
        return self.employee_repo.get_employee_by_id(employee_id)
