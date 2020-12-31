import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text, nullable=False)
    last_name = sa.Column(sa.Text, nullable=False)


class Student(Base):
    __tablename__ = "students"
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text, nullable=False)
    last_name = sa.Column(sa.Text, nullable=False)


class Homework(Base):
    __tablename__ = "homeworks"
    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.Text, nullable=False)
    date = sa.Column(sa.DateTime, default=datetime.datetime.utcnow, nullable=False)
    deadline = sa.Column(sa.Integer, nullable=False)
    author = sa.Column(sa.Integer, sa.ForeignKey(Teacher.id))
    is_done = sa.Column(sa.Boolean, nullable=False)
    checked_by = sa.Column(sa.Integer, sa.ForeignKey(Student.id))
