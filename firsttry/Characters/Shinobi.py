from firsttry.Characters.AbstractShinobi import AbstractShinobi


class Shinobi(AbstractShinobi):
    def __init__(self, name, health, power, taijutsu, ninjutsu, genjutsu, attack_strategy):
        super().__init__(name, health, power, taijutsu, ninjutsu, genjutsu)
        self.attack_strategy = attack_strategy

    def attack(self, target):
        self.attack_strategy.execute(self, target)

    def perform_taijutsu(self, target):
        damage = self.taijutsu * 5
        target.health -= damage
        print(f"{self.name} использует Тайдзюцу и наносит {damage} урона!")

    def perform_ninjutsu(self, target):
        damage = self.ninjutsu * 7
        target.health -= damage
        print(f"{self.name} использует Ниндзюцу и наносит {damage} урона!")

    def perform_genjutsu(self, target):
        damage = self.genjutsu * 4
        target.health -= damage / 2  # Гендзюцу может наносить меньше физического урона, но иметь другие эффекты
        print(f"{self.name} использует Гендзюцу и наносит {damage / 2} урона!")
