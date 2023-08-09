from firsttry.Battle.BattleStrategy import BattleStrategy


class Rasengan(BattleStrategy):
    def execute(self, attacker, target):
        damage = attacker.ninjutsu * 10  # просто пример
        target.health -= damage
        print(f"{attacker.name} использует Расенган и наносит {damage} урона!")