from app.interfaces.data_access import IITDepartmentRepository
from app.interfaces.services import IITDepartmentService


class ITDepartmentService(IITDepartmentService):
    def __init__(self, it_department_repo: IITDepartmentRepository):
        self.it_department_repo = it_department_repo

    def create_it_department(self, it_department: dict):
        self.it_department_repo.add_it_department(it_department)

    def it_departments_list(self):
        return self.it_department_repo.get_all_it_departments()

    def get_single_it_department(self, it_department_id: int):
        return self.it_department_repo.get_it_department_by_id(it_department_id)

    def edit_it_department(self, it_department_id: int, new_data: dict):
        return self.it_department_repo.edit_it_department(it_department_id, new_data)

    def delete_it_department(self, it_department_id):
        return self.it_department_repo.delete_it_department(it_department_id)
