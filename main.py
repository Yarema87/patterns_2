from models.database import init_db, SessionLocal
from models.repositories.employee_repo import EmployeeRepository
from models.repositories.mentor_repo import MentorRepository
from models.repositories.task_repo import TaskRepository
from models.repositories.feedback_repo import FeedbackRepository
from models.repositories.training_repo import TrainingRepository
from models.repositories.equipment_repo import EquipmentRepository
from models.repositories.hr_repo import HRManagerRepository
from models.repositories.department_repo import ITDepartmentRepository

from services.import_data import DataImportService


def main():
    init_db()
    session = SessionLocal()

    employee_repo = EmployeeRepository(session)
    mentor_repo = MentorRepository(session)
    task_repo = TaskRepository(session)
    feedback_repo = FeedbackRepository(session)
    training_repo = TrainingRepository(session)
    equipment_repo = EquipmentRepository(session)
    hr_repo = HRManagerRepository(session)
    it_repo = ITDepartmentRepository(session)

    import_service = DataImportService(
        employee_repo, mentor_repo, task_repo, feedback_repo,
        training_repo, equipment_repo, hr_repo, it_repo
    )

    import_service.import_from_csv("generated_data.csv")


if __name__ == "__main__":
    main()

