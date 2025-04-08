from sqlalchemy.orm import Session
from ..models import HRManager
from interfaces.data_access import IHRManagerRepository


class HRManagerRepository(IHRManagerRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_hr_manager(self, hr: HRManager):
        self.db.add(hr)
        self.db.commit()
        self.db.refresh(hr)

    def get_all_hr_managers(self):
        return self.db.query(HRManager).all()

    def get_hr_manager_by_id(self, hr_id: int):
        return self.db.query(HRManager).filter_by(id=hr_id).first()
