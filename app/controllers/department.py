from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import IITDepartmentService


def create_department_blueprint(department_service: IITDepartmentService):
    mod_department = Blueprint('department', __name__, url_prefix='/department')

    @mod_department.route('/', methods=['GET'])
    def departments_list():
        departments = department_service.it_departments_list()
        return render_template('department_list.html', departments=departments)

    @mod_department.route('/add', methods=['GET', 'POST'])
    def create_department():
        if request.method == 'POST':
            contacts = request.form['contacts']
            new_department = {'contacts': contacts}
            department_service.create_it_department(new_department)
            return redirect(url_for('department.departments_list'))
        return render_template('department_form.html')

    @mod_department.route('/get/<int:department_id>', methods=['GET'])
    def get_single_department(department_id: int):
        department = department_service.get_single_it_department(department_id)
        return render_template('single_department.html', department=department)

    @mod_department.route('/edit/<int:department_id>', methods=['GET', 'POST'])
    def edit_department(department_id: int):
        if request.method == 'POST':
            contacts = request.form['contacts']
            new_data = {'contacts': contacts}
            department_service.edit_it_department(department_id, new_data)
            return redirect(url_for('department.departments_list'))
        department = department_service.get_single_it_department(department_id)
        return render_template('department_form.html', department=department)

    @mod_department.route('/delete/<int:department_id>', methods=['POST'])
    def delete_department(department_id: int):
        department_service.delete_it_department(department_id)
        return redirect(url_for('department.departments_list'))

    return mod_department
