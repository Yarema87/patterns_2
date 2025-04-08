from interfaces.data_access import IFeedbackRepository
from interfaces.services import IFeedbackService
from models.models import Feedback


class FeedbackService(IFeedbackService):
    def __init__(self, feedback_repo: IFeedbackRepository):
        self.feedback_repo = feedback_repo

    def create_feedback(self, feedback: Feedback):
        self.feedback_repo.add_feedback(feedback)

    def feedback_list(self):
        return self.feedback_repo.get_all_feedbacks()

    def get_single_feedback(self, feedback_id: int):
        return self.feedback_repo.get_feedback_by_id(feedback_id)
