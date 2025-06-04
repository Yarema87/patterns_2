from sqlalchemy.orm import Session
from ..models import HRManager
from app.interfaces.data_access import IHRManagerRepository


class HRManagerRepository(IHRManagerRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_hr_manager(self, hr: dict):
        try:
            hr_to_add = HRManager(**hr)
            self.db.add(hr_to_add)
            self.db.commit()
            self.db.refresh(hr_to_add)
            return hr_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding HRManager: {e}")
            raise

    def get_all_hr_managers(self):
        return self.db.query(HRManager).all()

    def get_hr_manager_by_id(self, hr_id: int):
        return self.db.query(HRManager).filter_by(id=hr_id).first()

    def edit_hr_manager(self, hr_manager_id: int, new_data: dict):
        hr_manager = self.get_hr_manager_by_id(hr_manager_id)
        hr_manager.name = new_data['name']
        hr_manager.contacts = new_data['contacts']
        self.db.commit()

    def delete_hr_manager(self, hr_manager_id: int):
        hr_manager = self.get_hr_manager_by_id(hr_manager_id)
        self.db.delete(hr_manager)
        self.db.commit()
