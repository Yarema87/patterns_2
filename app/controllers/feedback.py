from flask import Blueprint, render_template, request, redirect, url_for
from app.interfaces.services import IFeedbackService
from app.models.models import Feedback
from datetime import datetime


def create_feedback_blueprint(feedback_service: IFeedbackService):
    mod_feedback = Blueprint('feedback', __name__, url_prefix='/feedbacks')

    @mod_feedback.route('/', methods=['GET'])
    def feedbacks_list():
        feedbacks = feedback_service.feedback_list()
        return render_template('feedback_list.html', feedbacks=feedbacks)

    @mod_feedback.route('/add', methods=['GET', 'POST'])
    def create_feedback():
        if request.method == 'POST':
            author_id = request.form['author_id']
            text = request.form['text']
            time_submission = datetime.strptime(request.form['time_submission'], '%Y-%m-%d %H:%M:%S')
            new_feedback = {'author_id': author_id, 'text': text, 'time_submission': time_submission}
            feedback_service.create_feedback(new_feedback)
            return redirect(url_for('feedback.feedbacks_list'))
        return render_template('feedback_form.html')

    @mod_feedback.route('/get/<int:feedback_id>', methods=['GET'])
    def get_single_feedback(feedback_id: int):
        feedback = feedback_service.get_single_feedback(feedback_id)
        return render_template('single_feedback.html', feedback=feedback)

    @mod_feedback.route('/edit/<int:feedback_id>', methods=['GET', 'POST'])
    def edit_feedback(feedback_id: int):
        if request.method == 'POST':
            author_id = request.form['author_id']
            text = request.form['text']
            time_submission = request.form['time_submission']
            new_data = {'author_id': author_id, 'text': text, 'time_submission': time_submission}
            feedback_service.edit_feedback(feedback_id, new_data)
            return redirect(url_for('feedback.feedbacks_list'))
        feedback = feedback_service.get_single_feedback(feedback_id)
        return render_template('feedback_form.html', feedback=feedback)

    @mod_feedback.route('/delete/<int:feedback_id>', methods=['POST'])
    def delete_feedback(feedback_id: int):
        feedback_service.delete_feedback(feedback_id)
        return redirect(url_for('feedback.feedbacks_list'))

    return mod_feedback
