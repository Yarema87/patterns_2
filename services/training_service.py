from interfaces.data_access import ITrainingRepository
from interfaces.services import ITrainingService
from models.models import Training


class TrainingService(ITrainingService):
    def __init__(self, training_repo: ITrainingRepository):
        self.training_repo = training_repo

    def create_training(self, training: Training):
        self.training_repo.add_training(training)

    def trainings_list(self):
        return self.training_repo.get_all_trainings()

    def get_single_training(self, training_id: int):
        return self.training_repo.get_training_by_id(training_id)
