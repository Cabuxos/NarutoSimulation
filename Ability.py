from abc import ABC, abstractmethod

class Ability(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Jutsu(Ability):
    def __init__(self, name, description, damage, сhakra_consumption):
        super().__init__(name, description)
        self.damage = damage
        self.сhakra_consumption = сhakra_consumption

    def perform(self):
        return f"used {self.name}!"


class Taijutsu(Jutsu):
    type = "Taijutsu"

    def __init__(self, name, description, damage, сhakra_consumption):
        super().__init__(name, description, damage, сhakra_consumption)


class Ninjustu(Jutsu):
    type = "Ninjutsu"

    def __init__(self, name, description, damage, сhakra_consumption, nature=None):
        super().__init__(name, description, damage, сhakra_consumption)
        self.nature = nature


class Genjutsu(Jutsu):
    type = "Genjutsu"

    def __init__(self, name, description, damage, сhakra_consumption):
        super().__init__(name, description, damage, сhakra_consumption)


class PassiveAbility(Ability):
    type = "Passive Ability"

    def __init__(self, name, description, bonus_chakra=0, bonus_health=0, bonus_taijutsu=0, bonus_ninjutsu_attack=0, bonus_genjutsu_attack=0):
        super().__init__(name, description)
        self.bonus_chakra = bonus_chakra
        self.bonus_health = bonus_health
        self.bonus_taijutsu = bonus_taijutsu
        self.bonus_ninjutsu_attack = bonus_ninjutsu_attack
        self.bonus_genjutsu_attack = bonus_genjutsu_attack


class ChakraBoost(PassiveAbility):
    def __init__(self, name, description):
        super().__init__(name, description, bonus_chakra=50)


class HealthBoost(PassiveAbility):
    def __init__(self, name, description):
        super().__init__(name, description, bonus_health=50)

