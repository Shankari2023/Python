from abc import ABC, abstractmethod

class dbabstract(ABC):
    @abstractmethod
    def create_engine(self):
        pass