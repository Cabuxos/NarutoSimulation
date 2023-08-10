from abc import ABC, abstractmethod
from typing import List
from Ability import PassiveAbility
from Jutsu import Jutsu


class Clan(ABC):
    def __init__(self, description, jutsus: List<Jutsu>, passive_abilities: List<PassiveAbility>):
        self.description = description
        self.jutsus = jutsus
        self.passive_abilities = passive_abilities

