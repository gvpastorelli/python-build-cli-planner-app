from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable,metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(ABC, Iterable):

    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):

    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

    def is_due(self):
        return self.date <= datetime.now()


        
# Create a class named DeadlinedMetaReminder that inherits from Iterable and 
# takes ABCMeta as its metaclass parameter. Add method is_due(), set the body to 
# pass and mark it with the @abstractmethod decorator