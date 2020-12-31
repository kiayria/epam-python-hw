"""Using ORM framework of your choice, create models classes created
in Homework 6 (Teachers, Students, Homework and others). -
Target database should be sqlite (filename main.db localted in current directory) -
ORM framework should support migrations.

Utilizing that framework capabilities,
create a migration file, creating all necessary database structures.
a migration file (separate) creating at least one record in each created database table
(*) optional task: write standalone script (get_report.py) that retrieves and stores the
following information into CSV file report.csv
for all done (completed) homeworks:
Student name (who completed homework) Creation date Teacher name who created homework

Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries."""

from models import Homework, Student, Teacher
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = sessionmaker()

engine = create_engine("sqlite:///main.db", echo=True)
# Base.metadata.create_all(bind=engine)
Session.configure(bind=engine)
session = Session()

print(engine.table_names())
for teacher in session.query(Teacher):
    print(teacher.id, teacher.first_name, teacher.last_name)

for student in session.query(Student):
    print(student.id, student.first_name, student.last_name)

for hw in session.query(Homework):
    print(hw.id, hw.text, hw.date, hw.deadline, hw.author, hw.is_done, hw.checked_by)
