from abc import ABC, abstractmethod


class AbstractMission(ABC):
    def __init__(self, level, tasks):
        self.level = level
        self.tasks = tasks

    @abstractmethod
    def is_completed(self):
        pass