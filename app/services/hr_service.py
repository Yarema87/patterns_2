from app.interfaces.data_access import IHRManagerRepository
from app.interfaces.services import IHRManagerService


class HRManagerService(IHRManagerService):
    def __init__(self, hr_manager_repo: IHRManagerRepository):
        self.hr_manager_repo = hr_manager_repo

    def create_hr_manager(self, hr_manager: dict):
        self.hr_manager_repo.add_hr_manager(hr_manager)

    def hr_managers_list(self):
        return self.hr_manager_repo.get_all_hr_managers()

    def get_single_hr_manager(self, hr_manager_id: int):
        return self.hr_manager_repo.get_hr_manager_by_id(hr_manager_id)

    def edit_hr_manager(self, hr_manager_id: int, new_data: dict):
        return self.hr_manager_repo.edit_hr_manager(hr_manager_id, new_data)

    def delete_hr_manager(self, hr_manager_id):
        return self.hr_manager_repo.delete_hr_manager(hr_manager_id)
