from sqlalchemy.orm import Session
from ..models import Feedback
from interfaces.data_access import IFeedbackRepository


class FeedbackRepository(IFeedbackRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_feedback(self, feedback: Feedback):
        self.db.add(feedback)
        self.db.commit()
        self.db.refresh(feedback)

    def get_all_feedbacks(self):
        return self.db.query(Feedback).all()

    def get_feedback_by_id(self, feedback_id: int):
        return self.db.query(Feedback).filter_by(id=feedback_id).first()
