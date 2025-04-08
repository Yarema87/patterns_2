from sqlalchemy.orm import Session
from ..models import Equipment
from interfaces.data_access import IEquipmentRepository


class EquipmentRepository(IEquipmentRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_equipment(self, equipment: Equipment):
        self.db.add(equipment)
        self.db.commit()
        self.db.refresh(equipment)

    def get_all_equipment(self):
        return self.db.query(Equipment).all()

    def get_equipment_by_id(self, equipment_id: int):
        return self.db.query(Equipment).filter_by(id=equipment_id).first()
