"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class ProjectException(Exception):
    """An exception base class for the project"""

    def __init__(self, message):
        self.message = message


class DeadlineError(ProjectException):
    """An exception class for overdue Homeworks"""


class Homework(object):
    """ Class Homework """

    def __init__(self, text: str, days_to_complete: int):
        """
        Constructor takes in following arguments:
            - text of the assignment
            - time period for completion (in days)
        """

        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = self.created + datetime.timedelta(days=days_to_complete)

    def is_active(self) -> bool:
        return datetime.datetime.now() < self.deadline


class HomeworkResult:
    """Class HomeworkResult"""

    def __init__(self, author, homework: Homework, solution: str):
        """
        Constructor takes in following arguments:
            - a Student object
            - a Homework object
            - an str that represents the solution of the task
        """
        if isinstance(author, Student):
            self.author = author
        else:
            raise ValueError("The parameter 'author' must of type Student.")

        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ValueError("The parameter 'homework' must be of type Homework.")

        if isinstance(solution, str):
            self.solution = solution
        else:
            raise ValueError("The parameter 'solution' must be of type str")

        self.created = datetime.datetime.now()


class Person:
    """
    This is a base class with following attributes:
        - first_name: str
        - last_name: str
    """

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name


class Teacher(Person):
    """Class Teacher"""

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, days_to_complete: int) -> Homework:
        """
        A method that creates an object of class Homework and returns it.
        """
        return Homework(text, days_to_complete)

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        if (
            len(homework_result.solution) < 5
            or homework_result.homework in self.homework_done
        ):
            return False
        else:
            self.homework_done[homework_result.homework] = homework_result
            return True

    @classmethod
    def reset_results(cls, homework_obj=None):
        if isinstance(homework_obj, Homework):
            cls.homework_done[homework_obj] = []
        else:
            cls.homework_done.clear()


class Student(Person):
    """ Class Student """

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        """
        A method that takes in an object of class Homework and returns HomeworkResult
        object if it is not overdue. In case it is, it raises an exception.
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late.")


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()