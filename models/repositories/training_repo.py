from sqlalchemy.orm import Session
from ..models import Training
from interfaces.data_access import ITrainingRepository


class TrainingRepository(ITrainingRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_training(self, training: Training):
        self.db.add(training)
        self.db.commit()
        self.db.refresh(training)

    def get_all_trainings(self):
        return self.db.query(Training).all()

    def get_training_by_id(self, training_id: int):
        return self.db.query(Training).filter_by(id=training_id).first()
