import pytest
from oop_task02.oop_task02 import (
    DeadlineError,
    HomeworkResult,
    Person,
    Student,
    Teacher,
)

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)
hw_late = opp_teacher.create_homework("Write a class", 0)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")


def test_homework_result_init_with_wrong_types_0():
    with pytest.raises(
        ValueError, match="The parameter 'author' must of type Student."
    ):
        HomeworkResult("not a Student object", oop_hw, "Solution")


def test_homework_result_init_with_wrong_types_1():
    with pytest.raises(
        ValueError, match="The parameter 'homework' must be of type Homework."
    ):
        HomeworkResult(good_student, "not a Homework object", "Solution")


def test_homework_result_init_with_wrong_types_2():
    with pytest.raises(
        ValueError, match="The parameter 'solution' must be of type str"
    ):
        HomeworkResult(good_student, oop_hw, 1)


def test_homework_done():
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_overdue_homework():
    with pytest.raises(DeadlineError, match="You are late."):
        lazy_student.do_homework(hw_late, "kinda done")


def test_reset_result():
    Teacher.reset_results()
    assert not Teacher.homework_done


def test_copied_homework():
    res_1 = good_student.do_homework(docs_hw, "Exactly the same solution")
    res_2 = lazy_student.do_homework(docs_hw, "Exactly the same solution")
    advanced_python_teacher.check_homework(res_1)
    advanced_python_teacher.check_homework(res_2)
    assert len(Teacher.homework_done) == 1


def test_check_inheritance():
    assert isinstance(opp_teacher, Person) and isinstance(good_student, Person)
