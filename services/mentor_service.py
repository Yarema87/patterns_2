from interfaces.data_access import IMentorRepository
from interfaces.services import IMentorService
from models.models import Mentor


class MentorService(IMentorService):
    def __init__(self, mentor_repo: IMentorRepository):
        self.mentor_repo = mentor_repo

    def create_mentor(self, mentor: Mentor):
        self.mentor_repo.add_mentor(mentor)

    def mentors_list(self):
        return self.mentor_repo.get_all_mentors()

    def get_single_mentor(self, mentor_id: int):
        return self.mentor_repo.get_mentor_by_id(mentor_id)
