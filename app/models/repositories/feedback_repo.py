from sqlalchemy.orm import Session
from ..models import Feedback
from app.interfaces.data_access import IFeedbackRepository
from datetime import datetime


class FeedbackRepository(IFeedbackRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_feedback(self, feedback: dict):
        try:
            feedback_to_add = Feedback(**feedback)
            self.db.add(feedback_to_add)
            self.db.commit()
            self.db.refresh(feedback_to_add)
            return feedback_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding Feedback: {e}")
            raise

    def get_all_feedbacks(self):
        return self.db.query(Feedback).all()

    def get_feedback_by_id(self, feedback_id: int):
        return self.db.query(Feedback).filter_by(id=feedback_id).first()

    def edit_feedback(self, feedback_id: int, new_data: dict):
        feedback = self.get_feedback_by_id(feedback_id)
        feedback.author_id = new_data['author_id']
        feedback.text = new_data['text']
        if isinstance(new_data['time_submission'], str):
            try:
                new_data['time_submission'] = datetime.strptime(new_data['time_submission'], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                new_data['time_submission'] = datetime.strptime(new_data['time_submission'], '%Y-%m-%d %H:%M:%S:%f')
            feedback.time_submission = new_data['time_submission']
        self.db.commit()

    def delete_feedback(self, feedback_id: int):
        feedback = self.get_feedback_by_id(feedback_id)
        self.db.delete(feedback)
        self.db.commit()
