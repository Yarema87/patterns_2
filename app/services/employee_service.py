from app.interfaces.data_access import IEmployeeRepository
from app.interfaces.services import IEmployeeService


class EmployeeService(IEmployeeService):
    def __init__(self, employee_repo: IEmployeeRepository):
        self.employee_repo = employee_repo

    def create_employee(self, employee: dict):
        self.employee_repo.add_employee(employee)

    def employees_list(self):
        return self.employee_repo.get_all_employees()

    def get_single_employee(self, employee_id: int):
        return self.employee_repo.get_employee_by_id(employee_id)

    def edit_employee(self, employee_id: int, new_data: dict):
        return self.employee_repo.edit_employee(employee_id, new_data)

    def delete_employee(self, employee_id):
        return self.employee_repo.delete_employee(employee_id)
