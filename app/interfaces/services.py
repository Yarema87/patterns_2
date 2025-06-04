from abc import ABC, abstractmethod


class IDataImportService(ABC):
    @abstractmethod
    def import_from_csv(self, filename):
        pass


class IEmployeeService(ABC):
    @abstractmethod
    def create_employee(self, employee: dict):
        pass

    @abstractmethod
    def employees_list(self):
        pass

    @abstractmethod
    def get_single_employee(self, employee_id: int):
        pass

    @abstractmethod
    def edit_employee(self, employee_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass


class IEquipmentService(ABC):
    @abstractmethod
    def create_equipment(self, equipment: dict):
        pass

    @abstractmethod
    def equipment_list(self):
        pass

    @abstractmethod
    def get_single_equipment(self, equipment_id: int):
        pass

    @abstractmethod
    def edit_equipment(self, equipment_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_equipment(self, equipment_id):
        pass


class IFeedbackService(ABC):
    @abstractmethod
    def create_feedback(self, feedback: dict):
        pass

    @abstractmethod
    def feedback_list(self):
        pass

    @abstractmethod
    def get_single_feedback(self, feedback_id: int):
        pass

    @abstractmethod
    def edit_feedback(self, feedback_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_feedback(self, feedback_id):
        pass


class IHRManagerService(ABC):
    @abstractmethod
    def create_hr_manager(self, hr_manager: dict):
        pass

    @abstractmethod
    def hr_managers_list(self):
        pass

    @abstractmethod
    def get_single_hr_manager(self, hr_manager_id: int):
        pass

    @abstractmethod
    def edit_hr_manager(self, hr_manager_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_hr_manager(self, hr_manager_id):
        pass


class IITDepartmentService(ABC):
    @abstractmethod
    def create_it_department(self, it_department: dict):
        pass

    @abstractmethod
    def it_departments_list(self):
        pass

    @abstractmethod
    def get_single_it_department(self, it_department_id: int):
        pass

    @abstractmethod
    def edit_it_department(self, it_department_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_it_department(self, it_department_id):
        pass


class IMentorService(ABC):
    @abstractmethod
    def create_mentor(self, mentor: dict):
        pass

    @abstractmethod
    def mentors_list(self):
        pass

    @abstractmethod
    def get_single_mentor(self, mentor_id: int):
        pass

    @abstractmethod
    def edit_mentor(self, mentor_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_mentor(self, mentor_id):
        pass


class ITaskService(ABC):
    @abstractmethod
    def create_task(self, task: dict):
        pass

    @abstractmethod
    def tasks_list(self):
        pass

    @abstractmethod
    def get_single_task(self, task_id: int):
        pass

    @abstractmethod
    def edit_task(self, task_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass


class ITrainingService(ABC):
    @abstractmethod
    def create_training(self, training: dict):
        pass

    @abstractmethod
    def trainings_list(self):
        pass

    @abstractmethod
    def get_single_training(self, training_id: int):
        pass

    @abstractmethod
    def edit_training(self, training_id: int, new_data: dict):
        pass

    @abstractmethod
    def delete_training(self, training_id):
        pass
