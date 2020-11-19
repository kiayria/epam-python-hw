from oop_task.homework import Homework


class Teacher(object):
    """
    Class Teacher
    """

    def __init__(self, first_name: str, last_name: str):
        """
        Constructor takes in 2 arguments:
            - first name : str
            - last name : str
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, days_to_complete: int) -> Homework:
        """
        A method that creates an object of class Homework and returns it.
        """
        return Homework(text, days_to_complete)
