from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import IEmployeeService


def create_employee_blueprint(employee_service: IEmployeeService):
    mod_employee = Blueprint('employee', __name__, url_prefix='/employees')

    @mod_employee.route('/', methods=['GET'])
    def employees_list():
        employees = employee_service.employees_list()
        return render_template('employee_list.html', employees=employees)

    @mod_employee.route('/add', methods=['GET', 'POST'])
    def create_employee():
        if request.method == 'POST':
            name = request.form['name']
            contacts = request.form['contacts']
            department = request.form['department']
            new_employee = {'name': name, 'contacts': contacts, 'department': department}
            employee_service.create_employee(new_employee)
            return redirect(url_for('employee.employees_list'))
        return render_template('employee_form.html')

    @mod_employee.route('/get/<int:employee_id>', methods=['GET'])
    def get_single_employee(employee_id: int):
        employee = employee_service.get_single_employee(employee_id)
        return render_template('single_employee.html', employee=employee)

    @mod_employee.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
    def edit_employee(employee_id: int):
        if request.method == 'POST':
            name = request.form['name']
            contacts = request.form['contacts']
            department = request.form['department']
            new_data = {'name': name, 'contacts': contacts, 'department': department}
            employee_service.edit_employee(employee_id, new_data)
            return redirect(url_for('employee.employees_list'))
        employee = employee_service.get_single_employee(employee_id)
        return render_template('employee_form.html', employee=employee)

    @mod_employee.route('/delete/<int:employee_id>', methods=['POST'])
    def delete_employee(employee_id: int):
        employee_service.delete_employee(employee_id)
        return redirect(url_for('employee.employees_list'))

    return mod_employee
