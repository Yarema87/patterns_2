from sqlalchemy.orm import Session
from ..models import Mentor
from app.interfaces.data_access import IMentorRepository


class MentorRepository(IMentorRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_mentor(self, mentor: dict):
        try:
            mentor_to_add = Mentor(**mentor)
            self.db.add(mentor_to_add)
            self.db.commit()
            self.db.refresh(mentor_to_add)
            return mentor_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding Mentor: {e}")
            raise

    def get_all_mentors(self):
        return self.db.query(Mentor).all()

    def get_mentor_by_id(self, mentor_id: int):
        return self.db.query(Mentor).filter_by(id=mentor_id).first()

    def edit_mentor(self, mentor_id: int, new_data: dict):
        mentor = self.get_mentor_by_id(mentor_id)
        mentor.name = new_data['name']
        mentor.contacts = new_data['contacts']
        mentor.mentor = new_data['mentor']
        mentor.mentee_id = new_data['mentee_id']
        self.db.commit()

    def delete_mentor(self, mentor_id: int):
        mentor = self.get_mentor_by_id(mentor_id)
        self.db.delete(mentor)
        self.db.commit()
