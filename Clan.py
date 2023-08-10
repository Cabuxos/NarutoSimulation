from abc import ABC, abstractmethod
from typing import List
from Ability import PassiveAbility
from Ability import Jutsu


class Clan(ABC):
    def __init__(self, name, description, jutsus: List[Jutsu], passive_abilities: List[PassiveAbility]):
        self.name = name
        self.description = description
        self.jutsus = jutsus
        self.passive_abilities = passive_abilities


