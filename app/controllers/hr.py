from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import IHRManagerService
from app.models.models import HRManager


def create_hr_blueprint(hr_service: IHRManagerService):
    mod_hr = Blueprint('hr', __name__, url_prefix='/hrs')

    @mod_hr.route('/', methods=['GET'])
    def hrs_list():
        hrs = hr_service.hr_managers_list()
        return render_template('hr_list.html', hrs=hrs)

    @mod_hr.route('/add', methods=['GET', 'POST'])
    def create_hr():
        if request.method == 'POST':
            name = request.form['name']
            contacts = request.form['contacts']
            new_hr = {'name': name, 'contacts': contacts}
            hr_service.create_hr_manager(new_hr)
            return redirect(url_for('hr.hrs_list'))
        return render_template('hr_form.html')

    @mod_hr.route('/get/<int:hr_id>', methods=['GET'])
    def get_single_hr(hr_id: int):
        hr = hr_service.get_single_hr_manager(hr_id)
        return render_template('single_hr.html', hr=hr)

    @mod_hr.route('/edit/<int:hr_id>', methods=['GET', 'POST'])
    def edit_hr(hr_id: int):
        if request.method == 'POST':
            name = request.form['name']
            contacts = request.form['contacts']
            new_data = {'name': name, 'contacts': contacts}
            hr_service.edit_hr_manager(hr_id, new_data)
            return redirect(url_for('hr.hrs_list'))
        hr = hr_service.get_single_hr_manager(hr_id)
        return render_template('hr_form.html', hr=hr)

    @mod_hr.route('/delete/<int:hr_id>', methods=['POST'])
    def delete_hr(hr_id: int):
        hr_service.delete_hr_manager(hr_id)
        return redirect(url_for('hr.hrs_list'))

    return mod_hr
