from abc import ABC, abstractmethod
from models.models import Employee, Task, Mentor, Feedback, Equipment, Training, HRManager, ITDepartment


class IEmployeeRepository(ABC):
    @abstractmethod
    def add_employee(self, employee: Employee):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id: int):
        pass


class ITaskRepository(ABC):
    @abstractmethod
    def add_task(self, task: Task):
        pass

    @abstractmethod
    def get_all_tasks(self):
        pass

    @abstractmethod
    def get_task_by_id(self, task_id: int):
        pass


class IMentorRepository(ABC):
    @abstractmethod
    def add_mentor(self, mentor: Mentor):
        pass

    @abstractmethod
    def get_all_mentors(self):
        pass

    @abstractmethod
    def get_mentor_by_id(self, mentor_id: int):
        pass


class IFeedbackRepository(ABC):
    @abstractmethod
    def add_feedback(self, feedback: Feedback):
        pass

    @abstractmethod
    def get_all_feedbacks(self):
        pass

    @abstractmethod
    def get_feedback_by_id(self, feedback_id: int):
        pass


class IEquipmentRepository(ABC):
    @abstractmethod
    def add_equipment(self, equipment: Equipment):
        pass

    @abstractmethod
    def get_all_equipment(self):
        pass

    @abstractmethod
    def get_equipment_by_id(self, equipment_id: int):
        pass


class ITrainingRepository(ABC):
    @abstractmethod
    def add_training(self, training: Training):
        pass

    @abstractmethod
    def get_all_trainings(self):
        pass

    @abstractmethod
    def get_training_by_id(self, training_id: int):
        pass


class IHRManagerRepository(ABC):
    @abstractmethod
    def add_hr_manager(self, hr: HRManager):
        pass

    @abstractmethod
    def get_all_hr_managers(self):
        pass

    @abstractmethod
    def get_hr_manager_by_id(self, hr_id: int):
        pass


class IITDepartmentRepository(ABC):
    @abstractmethod
    def add_it_department(self, department: ITDepartment):
        pass

    @abstractmethod
    def get_all_it_departments(self):
        pass

    @abstractmethod
    def get_it_department_by_id(self, department_id: int):
        pass
