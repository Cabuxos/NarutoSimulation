from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def execute(self, attacker, target):
        pass