from app.interfaces.data_access import IFeedbackRepository
from app.interfaces.services import IFeedbackService


class FeedbackService(IFeedbackService):
    def __init__(self, feedback_repo: IFeedbackRepository):
        self.feedback_repo = feedback_repo

    def create_feedback(self, feedback: dict):
        self.feedback_repo.add_feedback(feedback)

    def feedback_list(self):
        return self.feedback_repo.get_all_feedbacks()

    def get_single_feedback(self, feedback_id: int):
        return self.feedback_repo.get_feedback_by_id(feedback_id)

    def edit_feedback(self, feedback_id: int, new_data: dict):
        return self.feedback_repo.edit_feedback(feedback_id, new_data)

    def delete_feedback(self, feedback_id):
        return self.feedback_repo.delete_feedback(feedback_id)
