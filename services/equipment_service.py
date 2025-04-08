from interfaces.data_access import IEquipmentRepository
from interfaces.services import IEquipmentService
from models.models import Equipment


class EquipmentService(IEquipmentService):
    def __init__(self, equipment_repo: IEquipmentRepository):
        self.equipment_repo = equipment_repo

    def create_equipment(self, equipment: Equipment):
        self.equipment_repo.add_equipment(equipment)

    def equipment_list(self):
        return self.equipment_repo.get_all_equipment()

    def get_single_equipment(self, equipment_id: int):
        return self.equipment_repo.get_equipment_by_id(equipment_id)
