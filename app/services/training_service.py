from app.interfaces.data_access import ITrainingRepository
from app.interfaces.services import ITrainingService


class TrainingService(ITrainingService):
    def __init__(self, training_repo: ITrainingRepository):
        self.training_repo = training_repo

    def create_training(self, training: dict):
        self.training_repo.add_training(training)

    def trainings_list(self):
        return self.training_repo.get_all_trainings()

    def get_single_training(self, training_id: int):
        return self.training_repo.get_training_by_id(training_id)

    def edit_training(self, training_id: int, new_data: dict):
        return self.training_repo.edit_training(training_id, new_data)

    def delete_training(self, training_id):
        return self.training_repo.delete_training(training_id)
