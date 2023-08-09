from abc import ABC, abstractmethod
from typing import Literal


class Mission(ABC):
    def __init__(self, description, details, type: Literal["D", "C", "B", "A", "S"]):
        self.description = description
        self.details = details
        self.type = type
        self.XP = None

class Mission_S(Mission):
    def __init__(self, description, details, type="S"):
        super().__init__(description, details, type)
        self.XP = 100

class MissionFactory(ABC):
    @abstractmethod
    def create_mission(self, config):
        pass

class Mission_S_Factory(MissionFactory):
    def create_mission(self, config):
        return Mission_S(**config)
