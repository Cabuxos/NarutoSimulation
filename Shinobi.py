from typing import List
from Ability import Jutsu


class Shinobi():
    def __init__(self, name, abilities: List[Jutsu], clan: Clan = None):
        self.name = name
        self.abilities = abilities
        self.clan = clan
        self._basic_chakra_limit = 100
        self._basic_health_limit = 100

    #Дописать!!
    @property
    def chakra_limit(self):
        limit = self._basic_chakra_limit
        if self.clan:
            if "chakra_boost" in self.clan.passive_abilities:
                limit += 50
        return limit

    @property
    def health_limit(self):
        limit = self._basic_health_limit
        if self.clan:
            if "health_boost" in self.clan.passive_abilities:
                limit += 50
        return limit
