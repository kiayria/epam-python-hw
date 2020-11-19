from typing import Union

from oop_task.homework import Homework


class Student(object):
    """ Class Student """

    def __init__(self, first_name: str, last_name: str):
        """
        Constructor takes in 2 arguments:
            - first name
            - last name
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Union[Homework, None]:
        """
        A method that takes in an object of class Homework and returns it
        if it is not overdue. In case it is, it prints a message and
        returns None.
        """
        if homework.is_active():
            return homework
        else:
            print("You are late.")
            return None
