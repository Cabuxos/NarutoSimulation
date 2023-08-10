from abc import ABC, abstractmethod


class Ability(ABC):
    pass

class PassiveAbility(Ability):
    bonus_chakra = 0
    bonus_health = 0
    bonus_taijutsu = 0
    bonus_ninjutsu_attack = 0
    bonus_genjutsu_attack = 0


class ChakraBoost(PassiveAbility):
    bonus_chakra = 50


class HealthBoost(PassiveAbility):
    bonus_health = 50
