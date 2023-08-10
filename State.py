from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def handle(self, shinobi):
        pass


class NormalState(State):

    def handle(self, shinobi):
        print(f"{shinobi.name} is in normal state.")


class AttackingState(State):

    def handle(self, shinobi):
        print(f"{shinobi.name} is attacking!")


class DefendingState(State):

    def handle(self, shinobi):
        print(f"{shinobi.name} is defending!")


class MeditatingState(State):

    def handle(self, shinobi):
        print(f"{shinobi.name} is meditating to restore chakra.")