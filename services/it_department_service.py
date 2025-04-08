from interfaces.data_access import IITDepartmentRepository
from interfaces.services import IITDepartmentService
from models.models import ITDepartment


class ITDepartmentService(IITDepartmentService):
    def __init__(self, it_department_repo: IITDepartmentRepository):
        self.it_department_repo = it_department_repo

    def create_it_department(self, it_department: ITDepartment):
        self.it_department_repo.add_it_department(it_department)

    def it_departments_list(self):
        return self.it_department_repo.get_all_it_departments()

    def get_single_it_department(self, it_department_id: int):
        return self.it_department_repo.get_it_department_by_id(it_department_id)
