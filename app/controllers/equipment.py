from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import IEquipmentService
from app.models.models import Equipment


def create_equipment_blueprint(equipment_service: IEquipmentService):
    mod_equipment = Blueprint('equipment', __name__, url_prefix='/equipments')

    @mod_equipment.route('/', methods=['GET'])
    def equipments_list():
        equipments = equipment_service.equipment_list()
        return render_template('equipment_list.html', equipments=equipments)

    @mod_equipment.route('/add', methods=['GET', 'POST'])
    def create_equipment():
        if request.method == 'POST':
            type = request.form['type']
            assigned_to_id = request.form['assigned_to_id']
            new_equipment = {'type': type, 'assigned_to_id': assigned_to_id}
            equipment_service.create_equipment(new_equipment)
            return redirect(url_for('equipment.equipments_list'))
        return render_template('equipment_form.html')

    @mod_equipment.route('/get/<int:equipment_id>', methods=['GET'])
    def get_single_equipment(equipment_id: int):
        equipment = equipment_service.get_single_equipment(equipment_id)
        return render_template('single_equipment.html', equipment=equipment)

    @mod_equipment.route('/edit/<int:equipment_id>', methods=['GET', 'POST'])
    def edit_equipment(equipment_id: int):
        if request.method == 'POST':
            type = request.form['type']
            assigned_to_id = request.form['assigned_to_id']
            new_data = {'type': type, 'assigned_to_id': assigned_to_id}
            equipment_service.edit_equipment(equipment_id, new_data)
            return redirect(url_for('equipment.equipments_list'))
        equipment = equipment_service.get_single_equipment(equipment_id)
        return render_template('equipment_form.html', equipment=equipment)

    @mod_equipment.route('/delete/<int:equipment_id>', methods=['POST'])
    def delete_equipment(equipment_id: int):
        equipment_service.delete_equipment(equipment_id)
        return redirect(url_for('equipment.equipments_list'))

    return mod_equipment
