import csv
from models.models import Employee, Task, Mentor, Feedback, Equipment, Training, HRManager, ITDepartment
from interfaces.services import IDataImportService
from datetime import datetime


class DataImportService(IDataImportService):
    def __init__(self, employee_repo, mentor_repo, task_repo, feedback_repo, training_repo, equipment_repo,
                 hr_repo, it_repo):
        self.employee_repo = employee_repo
        self.mentor_repo = mentor_repo
        self.task_repo = task_repo
        self.feedback_repo = feedback_repo
        self.training_repo = training_repo
        self.equipment_repo = equipment_repo
        self.hr_repo = hr_repo
        self.it_repo = it_repo

    def import_from_csv(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(
                    name=row['employee_name'],
                    contacts=row['employee_contacts'],
                    department=row['employee_department']
                )
                self.employee_repo.add_employee(employee)
                mentor = Mentor(
                    name=row['mentor_name'],
                    contacts=row['mentor_contacts'],
                    department=row['mentor_department'],
                    mentee_id=row['mentee_id']
                )
                self.mentor_repo.add_mentor(mentor)
                deadline_str = row['task_deadline']
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
                task = Task(
                    title=row['task_title'],
                    description=row['task_description'],
                    deadline=deadline,
                    assigned_to_id=row['task_assigned_to']
                )
                self.task_repo.add_task(task)
                time_submission_str = row['feedback_time_submission']
                time_submission = datetime.fromisoformat(time_submission_str)
                feedback = Feedback(
                    author_id=row['feedback_author'],
                    text=row['feedback_text'],
                    time_submission=time_submission
                )
                self.feedback_repo.add_feedback(feedback)
                equipment = Equipment(
                    type=row['equipment_type'],
                    assigned_to_id=row['equipment_assigned_to']
                )
                self.equipment_repo.add_equipment(equipment)
                training = Training(
                    title=row['training_title']
                )
                self.training_repo.add_training(training)
                hr_manager = HRManager(
                    name=row['hr_name'],
                    contacts=row['hr_contacts']
                )
                self.hr_repo.add_hr_manager(hr_manager)
                it_department = ITDepartment(
                    contacts=row['it_contacts']
                )
                self.it_repo.add_it_department(it_department)
