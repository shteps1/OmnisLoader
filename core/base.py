from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def load(self):
        pass
