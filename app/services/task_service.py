from app.interfaces.data_access import ITaskRepository
from app.interfaces.services import ITaskService


class TaskService(ITaskService):
    def __init__(self, task_repo: ITaskRepository):
        self.task_repo = task_repo

    def create_task(self, task: dict):
        self.task_repo.add_task(task)

    def tasks_list(self):
        return self.task_repo.get_all_tasks()

    def get_single_task(self, task_id: int):
        return self.task_repo.get_task_by_id(task_id)

    def edit_task(self, task_id: int, new_data: dict):
        return self.task_repo.edit_task(task_id, new_data)

    def delete_task(self, task_id):
        return self.task_repo.delete_task(task_id)
