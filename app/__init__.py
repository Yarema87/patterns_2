from flask import Flask, render_template
from app.models.database import SessionLocal


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret-key'

    app.session = SessionLocal()

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    from app.controllers.employee import create_employee_blueprint
    from app.controllers.department import create_department_blueprint
    from app.controllers.task import create_task_blueprint
    from app.controllers.training import create_training_blueprint
    from app.controllers.feedback import create_feedback_blueprint
    from app.controllers.equipment import create_equipment_blueprint
    from app.controllers.mentor import create_mentor_blueprint
    from app.controllers.hr import create_hr_blueprint
    from app.controllers.home import mode_home

    from app.models.repositories.employee_repo import EmployeeRepository
    from app.models.repositories.training_repo import TrainingRepository
    from app.models.repositories.task_repo import TaskRepository
    from app.models.repositories.mentor_repo import MentorRepository
    from app.models.repositories.hr_repo import HRManagerRepository
    from app.models.repositories.department_repo import ITDepartmentRepository
    from app.models.repositories.equipment_repo import EquipmentRepository
    from app.models.repositories.feedback_repo import FeedbackRepository

    from app.services.employee_service import EmployeeService
    from app.services.hr_service import HRManagerService
    from app.services.equipment_service import EquipmentService
    from app.services.feedback_service import FeedbackService
    from app.services.it_department_service import ITDepartmentService
    from app.services.task_service import TaskService
    from app.services.mentor_service import MentorService
    from app.services.training_service import TrainingService

    employee_service = EmployeeService(EmployeeRepository(app.session))
    mentor_service = MentorService(MentorRepository(app.session))
    hr_service = HRManagerService(HRManagerRepository(app.session))
    equipment_service = EquipmentService(EquipmentRepository(app.session))
    task_service = TaskService(TaskRepository(app.session))
    feedback_service = FeedbackService(FeedbackRepository(app.session))
    department_service = ITDepartmentService(ITDepartmentRepository(app.session))
    training_service = TrainingService(TrainingRepository(app.session))

    mod_employee = create_employee_blueprint(employee_service)
    mod_mentor = create_mentor_blueprint(mentor_service)
    mod_hr = create_hr_blueprint(hr_service)
    mod_equipment = create_equipment_blueprint(equipment_service)
    mod_task = create_task_blueprint(task_service)
    mod_feedback = create_feedback_blueprint(feedback_service)
    mod_department = create_department_blueprint(department_service)
    mod_training = create_training_blueprint(training_service)

    app.register_blueprint(mod_employee)
    app.register_blueprint(mode_home)
    app.register_blueprint(mod_mentor)
    app.register_blueprint(mod_hr)
    app.register_blueprint(mod_equipment)
    app.register_blueprint(mod_task)
    app.register_blueprint(mod_feedback)
    app.register_blueprint(mod_department)
    app.register_blueprint(mod_training)

    return app
