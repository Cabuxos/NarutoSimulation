from typing import List
from Jutsu import Jutsu


class Shinobi():
    def __init__(self, name, abilities: List[Jutsu], clan: Clan = None):
        self.name = name
        self.abilities = abilities
        self.clan = clan
        self._basic_chakra_limit = 100

    #Дописать!!
    @property
    def chakra_limit(self):
        limit = self._basic_chakra_limit
        if self.clan:
            if "increase_chakra_limit" in self.clan.passive_abilities:
                limit += 50
        return limit
