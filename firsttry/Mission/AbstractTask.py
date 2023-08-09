from abc import ABC, abstractmethod


class AbstractTask(ABC):
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    @abstractmethod
    def complete(self):
        pass