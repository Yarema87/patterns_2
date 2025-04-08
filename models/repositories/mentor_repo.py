from sqlalchemy.orm import Session
from ..models import Mentor
from interfaces.data_access import IMentorRepository


class MentorRepository(IMentorRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_mentor(self, mentor: Mentor):
        self.db.add(mentor)
        self.db.commit()
        self.db.refresh(mentor)

    def get_all_mentors(self):
        return self.db.query(Mentor).all()

    def get_mentor_by_id(self, mentor_id: int):
        return self.db.query(Mentor).filter_by(id=mentor_id).first()
