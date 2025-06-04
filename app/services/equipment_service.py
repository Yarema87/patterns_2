from app.interfaces.data_access import IEquipmentRepository
from app.interfaces.services import IEquipmentService


class EquipmentService(IEquipmentService):
    def __init__(self, equipment_repo: IEquipmentRepository):
        self.equipment_repo = equipment_repo

    def create_equipment(self, equipment: dict):
        self.equipment_repo.add_equipment(equipment)

    def equipment_list(self):
        return self.equipment_repo.get_all_equipment()

    def get_single_equipment(self, equipment_id: int):
        return self.equipment_repo.get_equipment_by_id(equipment_id)

    def edit_equipment(self, equipment_id: int, new_data: dict):
        return self.equipment_repo.edit_equipment(equipment_id, new_data)

    def delete_equipment(self, equipment_id):
        return self.equipment_repo.delete_equipment(equipment_id)
