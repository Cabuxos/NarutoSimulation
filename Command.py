from abc import ABC, abstractmethod


# Интерфейс команды
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# Конкретные команды
class MoveForwardCommand(Command):

    def __init__(self, shinobi):
        self.shinobi = shinobi

    def execute(self):
        print(f"{self.shinobi.name} is moving forward!")

class MoveBackwardsCommand(Command):
    def __init__(self, shinobi):
        self.shinobi = shinobi

    def execute(self):
        print(f"{self.shinobi.name} is moving backwards!")

class MoveLeftCommand(Command):
    def __init__(self, shinobi):
        self.shinobi = shinobi

    def execute(self):
        print(f"{self.shinobi.name} is moving left!")


class MoveRightCommand(Command):
    def __init__(self, shinobi):
        self.shinobi = shinobi

    def execute(self):
        print(f"{self.shinobi.name} is moving right!")

class AttackCommand(Command):

    def __init__(self, shinobi):
        self.shinobi = shinobi

    def execute(self):
        print(f"{self.shinobi.name} is attacking!")

# Вызывающий
class CommandInvoker:

    def __init__(self, command):
        self._command = command

    def set_command(self, command):
        self._command = command

    def action(self):
        self._command.execute()
