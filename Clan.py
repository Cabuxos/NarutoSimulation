from abc import ABC, abstractmethod

class Clan(ABC):
    @abstractmethod
    def special_ability(self):
        pass