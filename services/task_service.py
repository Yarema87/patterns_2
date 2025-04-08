from interfaces.data_access import ITaskRepository
from interfaces.services import ITaskService
from models.models import Task


class TaskService(ITaskService):
    def __init__(self, task_repo: ITaskRepository):
        self.task_repo = task_repo

    def create_task(self, task: Task):
        self.task_repo.add_task(task)

    def tasks_list(self):
        return self.task_repo.get_all_tasks()

    def get_single_task(self, task_id: int):
        return self.task_repo.get_task_by_id(task_id)
