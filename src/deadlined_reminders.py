from abc import ABCMeta, abstractmethod
from collections.abc import Iterable

class DeadlinedMetaReminder(Iterable):
    pass

# Create a class named DeadlinedMetaReminder that inherits from Iterable and 
# takes ABCMeta as its metaclass parameter. Add method is_due(), set the body to 
# pass and mark it with the @abstractmethod decorator.