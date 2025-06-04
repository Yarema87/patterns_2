from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import ITaskService
from app.models.models import Task
from datetime import datetime


def create_task_blueprint(task_service: ITaskService):
    mod_task = Blueprint('task', __name__, url_prefix='/tasks')

    @mod_task.route('/', methods=['GET'])
    def tasks_list():
        tasks = task_service.tasks_list()
        return render_template('tasks_list.html', tasks=tasks)

    @mod_task.route('/add', methods=['GET', 'POST'])
    def create_task():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d %H:%M:%S')
            assigned_to_id = request.form['assigned_to_id']
            new_task = {'title': title, 'description': description, 'deadline': deadline, 'assigned_to_id': assigned_to_id}
            task_service.create_task(new_task)
            return redirect(url_for('task.tasks_list'))
        return render_template('task_form.html')

    @mod_task.route('/get/<int:task_id>', methods=['GET'])
    def get_single_task(task_id: int):
        task = task_service.get_single_task(task_id)
        return render_template('single_task.html', task=task)

    @mod_task.route('/edit/<int:task_id>', methods=['GET', 'POST'])
    def edit_task(task_id: int):
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            deadline = request.form['deadline']
            assigned_to_id = request.form['assigned_to_id']
            new_data = {'title': title, 'description': description, 'deadline': deadline, 'assigned_to_id': assigned_to_id}
            task_service.edit_task(task_id, new_data)
            return redirect(url_for('task.tasks_list'))
        task = task_service.get_single_task(task_id)
        return render_template('task_form.html', task=task)

    @mod_task.route('/delete/<int:task_id>', methods=['POST'])
    def delete_task(task_id: int):
        task_service.delete_task(task_id)
        return redirect(url_for('task.tasks_list'))

    return mod_task
