from firsttry.Characters.Entity import Entity
from abc import abstractmethod


class AbstractShinobi(Entity):
    def __init__(self, name, health, power, taijutsu, ninjutsu, genjutsu):
        super().__init__(name, health, power)
        self.taijutsu = taijutsu
        self.ninjutsu = ninjutsu
        self.genjutsu = genjutsu

    @abstractmethod
    def perform_taijutsu(self, target):
        pass

    @abstractmethod
    def perform_ninjutsu(self, target):
        pass

    @abstractmethod
    def perform_genjutsu(self, target):
        pass
