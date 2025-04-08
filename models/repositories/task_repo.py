from sqlalchemy.orm import Session
from ..models import Task
from interfaces.data_access import ITaskRepository


class TaskRepository(ITaskRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_task(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

    def get_all_tasks(self):
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int):
        return self.db.query(Task).filter_by(id=task_id).first()