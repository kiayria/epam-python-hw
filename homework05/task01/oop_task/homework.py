import datetime


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
