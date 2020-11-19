import datetime

import pytest
from oop_task.homework import Homework
from oop_task.student import Student
from oop_task.teacher import Teacher


@pytest.mark.parametrize(
    ["name", "surname", "expected_name", "expected_surname"],
    [
        ("Sylvanas", "Windrunner", "Sylvanas", "Windrunner"),
        ("Lor'themar", "Theron", "Lor'themar", "Theron"),
        ("Baine", "Bloodhoof", "Baine", "Bloodhoof"),
    ],
)
def test_teacher_class_constructor(name, surname, expected_name, expected_surname):
    teacher = Teacher(name, surname)
    assert getattr(teacher, "first_name") == expected_name
    assert getattr(teacher, "last_name") == expected_surname


@pytest.mark.parametrize(
    ["text", "days_to_complete"],
    [("Learn Algorithms", 0), ("Learn OOP", 5), ("Learn OS", 10)],
)
def test_teacher_create_homework(text, days_to_complete):
    teacher = Teacher("Test", "Test")
    homework = teacher.create_homework(text, days_to_complete)
    assert getattr(homework, "text") == text
    assert getattr(homework, "deadline") == getattr(
        homework, "created"
    ) + datetime.timedelta(days=days_to_complete)


@pytest.mark.parametrize(
    ["name", "surname", "expected_name", "expected_surname"],
    [
        ("Anduin", "Wrynn", "Anduin", "Wrynn"),
        ("Jaina", "Proudmoore", "Jaina", "Proudmoore"),
        ("Genn", "Greymane", "Genn", "Greymane"),
    ],
)
def test_student_class_constructor(name, surname, expected_name, expected_surname):
    student = Student(name, surname)
    assert getattr(student, "first_name") == expected_name
    assert getattr(student, "last_name") == expected_surname


@pytest.mark.parametrize(
    "homework",
    [
        Homework("Learn Algorithms", 1),
        Homework("Learn OOP", 3),
        Homework("Learn OS", 5),
    ],
)
def test_student_do_homework_positive(homework):
    student = Student("Test", "Test")
    assert student.do_homework(homework) == homework


@pytest.mark.parametrize(
    "homework",
    [
        Homework("Learn Algorithms", 0),
        Homework("Learn OOP", 0),
        Homework("Learn OS", 0),
    ],
)
def test_student_do_homework_negative(homework):
    student = Student("Test", "Test")
    assert student.do_homework(homework) is None


@pytest.mark.parametrize(
    ["text", "days_to_complete"],
    [("Learn Algorithms", 0), ("Learn OOP", 5), ("Learn OS", 10)],
)
def test_homework_constructor(text, days_to_complete):
    homework = Homework(text, days_to_complete)
    assert getattr(homework, "text") == text
    assert getattr(homework, "deadline") == getattr(
        homework, "created"
    ) + datetime.timedelta(days=days_to_complete)


@pytest.mark.parametrize(
    ["text", "days_to_complete"],
    [("Learn Algorithms", 0.01), ("Learn OOP", 5), ("Learn OS", 10)],
)
def test_homework_is_active_positive(text, days_to_complete):
    homework = Homework(text, days_to_complete)
    assert homework.is_active() is True


@pytest.mark.parametrize(
    ["text", "days_to_complete"],
    [("Learn Algorithms", 0), ("Learn OOP", -1), ("Learn OS", -5)],
)
def test_homework_is_active_positive(text, days_to_complete):
    homework = Homework(text, days_to_complete)
    assert homework.is_active() is False
