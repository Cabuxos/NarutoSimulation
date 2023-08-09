from firsttry.Battle.BattleStrategy import BattleStrategy


class Chidori(BattleStrategy):
    def execute(self, attacker, target):
        damage = attacker.ninjutsu * 12  # просто пример
        target.health -= damage
        print(f"{attacker.name} использует Чидори и наносит {damage} урона!")