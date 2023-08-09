from abc import ABC, abstractmethod


class Jutsu(ABC):
    def __init__(self, name, type, damage, stress):
        self.name = name
        self.type = type
        self.damage = damage
        self.stress = stress

    def perform(self):
        return f"used {self.name}!"


class Taijutsu(Jutsu):
    def __init__(self, name, type, damage, stress):
        super().__init__(name, type, damage, stress)


class Ninjustu(Jutsu):
    def __init__(self, name, type, damage, stress, nature=None):
        super().__init__(name, type, damage, stress)
        self.nature = nature


class Genjutsu(Jutsu):
    def __init__(self, name, type, damage, stress):
        super().__init__(name, type, damage, stress)
