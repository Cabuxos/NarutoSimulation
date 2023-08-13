from abc import ABC, abstractmethod


class Modification(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ArmorModification(Modification):
    def apply_to(self, shinobi):
        shinobi._basic_health_limit += 30

    def remove_from(self, shinobi):
        shinobi._basic_health_limit -= 30

class ChakraBoostModificacion(Modification):
    def apply_to(self, shinobi):
        shinobi.chakra_limit += 30

    def remove_from(self, shinobi):
        shinobi.chakra_limit -= 30