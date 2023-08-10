from typing import List
from Ability import Jutsu
from Clan import Clan
from State import NormalState


class Shinobi():
    def __init__(self, name, abilities: List[Jutsu], clan: Clan = None):
        self.name = name
        self._state = NormalState()
        self.abilities = abilities
        self.modifications = []
        self.clan = clan
        self._basic_chakra_limit = 100
        self._basic_health_limit = 100

    def apply_modification(self, mod):
        if mod not in self.modifications:
            mod.apply_to(self)
            self.modifications.append(mod)

    def remove_modification(self, mod):
        if mod in self.modifications:
            mod.remove_from(self)
            self.modifications.remove(mod)

    def set_state(self, state):
        self._state = state

    def handle(self):
        self._state.handle(self)

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
