from sqlalchemy.orm import Session
from ..models import Equipment
from app.interfaces.data_access import IEquipmentRepository


class EquipmentRepository(IEquipmentRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_equipment(self, equipment: dict):
        try:
            equipment_to_add = Equipment(**equipment)
            self.db.add(equipment_to_add)
            self.db.commit()
            self.db.refresh(equipment_to_add)
            return equipment_to_add
        except Exception as e:
            self.db.rollback()
            print(f"Error while adding Equipment: {e}")
            raise

    def get_all_equipment(self):
        return self.db.query(Equipment).all()

    def get_equipment_by_id(self, equipment_id: int):
        return self.db.query(Equipment).filter_by(id=equipment_id).first()

    def edit_equipment(self, equipment_id: int, new_data: dict):
        equipment = self.get_equipment_by_id(equipment_id)
        equipment.type = new_data['type']
        equipment.assigned_to_id = new_data['assigned_to_id']
        self.db.commit()

    def delete_equipment(self, equipment_id: int):
        equipment = self.get_equipment_by_id(equipment_id)
        self.db.delete(equipment)
        self.db.commit()
