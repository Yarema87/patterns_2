from sqlalchemy.orm import Session
from ..models import ITDepartment
from app.interfaces.data_access import IITDepartmentRepository


class ITDepartmentRepository(IITDepartmentRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_it_department(self, department: dict):
        try:
            department_to_add = ITDepartment(**department)
            self.db.add(department_to_add)
            self.db.commit()
            self.db.refresh(department_to_add)
            return department_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding ITDepartment: {e}")
            raise

    def get_all_it_departments(self):
        return self.db.query(ITDepartment).all()

    def get_it_department_by_id(self, department_id: int):
        return self.db.query(ITDepartment).filter_by(id=department_id).first()

    def edit_it_department(self, it_department_id: int, new_data: dict):
        it_department = self.get_it_department_by_id(it_department_id)
        it_department.contacts = new_data['contacts']
        self.db.commit()

    def delete_it_department(self, it_department_id: int):
        it_department = self.get_it_department_by_id(it_department_id)
        self.db.delete(it_department)
        self.db.commit()
