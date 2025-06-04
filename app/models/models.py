
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.types import Text

Base = declarative_base()

training_tasks = Table(
    "training_tasks",
    Base.metadata,
    Column("training_id", ForeignKey("training.id"), primary_key=True),
    Column("task_id", ForeignKey("task.id"), primary_key=True)
)


class HRManager(Base):
    __tablename__ = "hrmanager"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contacts = Column(String)


class ITDepartment(Base):
    __tablename__ = "itdepartment"

    id = Column(Integer, primary_key=True)
    contacts = Column(String)


class Mentor(Base):
    __tablename__ = "mentor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contacts = Column(String)
    department = Column(String)
    mentee_id = Column(Integer, ForeignKey("employee.id"))
    mentee = relationship("Employee", back_populates="mentor")


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contacts = Column(String)
    department = Column(String)

    tasks = relationship("Task", back_populates="assigned_to")
    feedback_given = relationship("Feedback", back_populates="author")
    equipment = relationship("Equipment", back_populates="assigned_to")
    mentor = relationship("Mentor", back_populates="mentee", uselist=False)


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    deadline = Column(DateTime)
    assigned_to_id = Column(Integer, ForeignKey("employee.id"))
    assigned_to = relationship("Employee", back_populates="tasks")


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("employee.id"))
    author = relationship("Employee", back_populates="feedback_given")
    text = Column(Text)
    time_submission = Column(DateTime)


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    assigned_to_id = Column(Integer, ForeignKey("employee.id"))
    assigned_to = relationship("Employee", back_populates="equipment")


class Training(Base):
    __tablename__ = "training"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    tasks = relationship("Task", secondary=training_tasks)
