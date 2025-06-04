from sqlalchemy.orm import Session
from ..models import Training
from app.interfaces.data_access import ITrainingRepository


class TrainingRepository(ITrainingRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_training(self, training: dict):
        try:
            training_to_add = Training(**training)
            self.db.add(training_to_add)
            self.db.commit()
            self.db.refresh(training_to_add)
            return training_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding Training: {e}")
            raise

    def get_all_trainings(self):
        return self.db.query(Training).all()

    def get_training_by_id(self, training_id: int):
        return self.db.query(Training).filter_by(id=training_id).first()

    def edit_training(self, training_id: int, new_data: dict):
        training = self.get_training_by_id(training_id)
        training.title = new_data['title']
        self.db.commit()

    def delete_training(self, training_id: int):
        training = self.get_training_by_id(training_id)
        self.db.delete(training)
        self.db.commit()
