from app.interfaces.data_access import IMentorRepository
from app.interfaces.services import IMentorService


class MentorService(IMentorService):
    def __init__(self, mentor_repo: IMentorRepository):
        self.mentor_repo = mentor_repo

    def create_mentor(self, mentor: dict):
        self.mentor_repo.add_mentor(mentor)

    def mentors_list(self):
        return self.mentor_repo.get_all_mentors()

    def get_single_mentor(self, mentor_id: int):
        return self.mentor_repo.get_mentor_by_id(mentor_id)

    def edit_mentor(self, mentor_id: int, new_data: dict):
        return self.mentor_repo.edit_mentor(mentor_id, new_data)

    def delete_mentor(self, mentor_id):
        return self.mentor_repo.delete_mentor(mentor_id)
