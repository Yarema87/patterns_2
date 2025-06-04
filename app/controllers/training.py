from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import ITrainingService
from app.models.models import Training


def create_training_blueprint(training_service: ITrainingService):
    mod_training = Blueprint('training', __name__, url_prefix='/trainings')

    @mod_training.route('/', methods=['GET'])
    def trainings_list():
        trainings = training_service.trainings_list()
        return render_template('training_list.html', trainings=trainings)

    @mod_training.route('/add', methods=['GET', 'POST'])
    def create_training():
        if request.method == 'POST':
            title = request.form['title']
            new_training = {'title': title}
            training_service.create_training(new_training)
            return redirect(url_for('training.trainings_list'))
        return render_template('training_form.html')

    @mod_training.route('/get/<int:training_id>', methods=['GET'])
    def get_single_training(training_id: int):
        training = training_service.get_single_training(training_id)
        return render_template('single_training.html', training=training)

    @mod_training.route('/edit/<int:training_id>', methods=['GET', 'POST'])
    def edit_training(training_id: int):
        if request.method == 'POST':
            title = request.form['title']
            new_data = {'title': title}
            training_service.edit_training(training_id, new_data)
            return redirect(url_for('training.trainings_list'))
        training = training_service.get_single_training(training_id)
        return render_template('training_form.html', training=training)

    @mod_training.route('/delete/<int:training_id>', methods=['POST'])
    def delete_training(training_id: int):
        training_service.delete_training(training_id)
        return redirect(url_for('training.trainings_list'))

    return mod_training
