from sqlalchemy.orm import Session
from ..models import Task
from app.interfaces.data_access import ITaskRepository
from datetime import datetime


class TaskRepository(ITaskRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_task(self, task: dict):
        try:
            task_to_add = Task(**task)
            self.db.add(task_to_add)
            self.db.commit()
            self.db.refresh(task_to_add)
            return task_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding Task: {e}")
            raise

    def get_all_tasks(self):
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int):
        return self.db.query(Task).filter_by(id=task_id).first()

    def edit_task(self, task_id: int, new_data: dict):
        task = self.get_task_by_id(task_id)
        task.title = new_data['title']
        task.description = new_data['description']
        task.assigned_to_id = new_data['assigned_to_id']
        if isinstance(new_data['deadline'], str):
            new_data['deadline'] = datetime.strptime(new_data['deadline'], '%Y-%m-%d %H:%M:%S')
            task.deadline = new_data['deadline']
        self.db.commit()

    def delete_task(self, task_id: int):
        task = self.get_task_by_id(task_id)
        self.db.delete(task)
        self.db.commit()
