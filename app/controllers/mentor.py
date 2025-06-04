from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import IMentorService
from app.models.models import Mentor


def create_mentor_blueprint(mentor_service: IMentorService):
    mod_mentor = Blueprint('mentor', __name__, url_prefix='/mentors')

    @mod_mentor.route('/', methods=['GET'])
    def mentors_list():
        mentors = mentor_service.mentors_list()
        return render_template('mentor_list.html', mentors=mentors)

    @mod_mentor.route('/add', methods=['GET', 'POST'])
    def create_mentor():
        if request.method == 'POST':
            name = request.form['name']
            contacts = request.form['contacts']
            department = request.form['department']
            mentee_id = request.form['mentee_id']
            new_mentor = {'name': name, 'contacts': contacts, 'department': department, 'mentee_id': mentee_id}
            mentor_service.create_mentor(new_mentor)
            return redirect(url_for('mentor.mentors_list'))
        return render_template('mentor_form.html')

    @mod_mentor.route('/get/<int:mentor_id>', methods=['GET'])
    def get_single_mentor(mentor_id: int):
        mentor = mentor_service.get_single_mentor(mentor_id)
        return render_template('single_mentor.html', mentor=mentor)

    @mod_mentor.route('/edit/<int:mentor_id>', methods=['GET', 'POST'])
    def edit_mentor(mentor_id: int):
        if request.method == 'POST':
            name = request.form['name']
            contacts = request.form['contacts']
            department = request.form['department']
            mentee_id = request.form['mentee_id']
            new_data = {'name': name, 'contacts': contacts, 'department': department, 'mentee_id': mentee_id}
            mentor_service.edit_mentor(mentor_id, new_data)
            return redirect(url_for('mentor.mentors_list'))
        mentor = mentor_service.get_single_mentor(mentor_id)
        return render_template('mentor_form.html', mentor=mentor)

    @mod_mentor.route('/delete/<int:mentor_id>', methods=['POST'])
    def delete_mentor(mentor_id: int):
        mentor_service.delete_mentor(mentor_id)
        return redirect(url_for('mentor.mentors_list'))

    return mod_mentor
