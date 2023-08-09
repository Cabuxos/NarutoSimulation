from typing import List
from Jutsu import Jutsu


class Shinobi():
    def __init__(self, name, abilities: List[Jutsu]):
        self.name = name
        self.abilities = abilities