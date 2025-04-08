from sqlalchemy.orm import Session
from ..models import ITDepartment
from interfaces.data_access import IITDepartmentRepository


class ITDepartmentRepository(IITDepartmentRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_it_department(self, department: ITDepartment):
        self.db.add(department)
        self.db.commit()
        self.db.refresh(department)

    def get_all_it_departments(self):
        return self.db.query(ITDepartment).all()

    def get_it_department_by_id(self, department_id: int):
        return self.db.query(ITDepartment).filter_by(id=department_id).first()
