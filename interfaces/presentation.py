from abc import ABC, abstractmethod
from models.models import Employee, Equipment, Feedback, HRManager, ITDepartment, Mentor, Task, Training


class IEmployeePresentation(ABC):
    @abstractmethod
    def create_employee(self, employee: Employee):
        pass

    @abstractmethod
    def employees_list(self):
        pass

    @abstractmethod
    def get_single_employee(self, employee_id: int):
        pass


class IEquipmentPresentation(ABC):
    @abstractmethod
    def create_equipment(self, equipment: Equipment):
        pass

    @abstractmethod
    def equipment_list(self):
        pass

    @abstractmethod
    def get_single_equipment(self, equipment_id: int):
        pass


class IFeedbackPresentation(ABC):
    @abstractmethod
    def create_feedback(self, feedback: Feedback):
        pass

    @abstractmethod
    def feedback_list(self):
        pass

    @abstractmethod
    def get_single_feedback(self, feedback_id: int):
        pass


class IHRManagerPresentation(ABC):
    @abstractmethod
    def create_hr_manager(self, hr_manager: HRManager):
        pass

    @abstractmethod
    def hr_managers_list(self):
        pass

    @abstractmethod
    def get_single_hr_manager(self, hr_manager_id: int):
        pass


class IITDepartmentPresentation(ABC):
    @abstractmethod
    def create_it_department(self, it_department: ITDepartment):
        pass

    @abstractmethod
    def it_departments_list(self):
        pass

    @abstractmethod
    def get_single_it_department(self, it_department_id: int):
        pass


class IMentorPresentation(ABC):
    @abstractmethod
    def create_mentor(self, mentor: Mentor):
        pass

    @abstractmethod
    def mentors_list(self):
        pass

    @abstractmethod
    def get_single_mentor(self, mentor_id: int):
        pass


class ITaskPresentation(ABC):
    @abstractmethod
    def create_task(self, task: Task):
        pass

    @abstractmethod
    def tasks_list(self):
        pass

    @abstractmethod
    def get_single_task(self, task_id: int):
        pass


class ITrainingPresentation(ABC):
    @abstractmethod
    def create_training(self, training: Training):
        pass

    @abstractmethod
    def trainings_list(self):
        pass

    @abstractmethod
    def get_single_training(self, training_id: int):
        pass
