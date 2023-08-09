from abc import ABC, abstractmethod


class AbstractMissionFactory(ABC):
    @abstractmethod
    def create_mission(self, level):
        pass