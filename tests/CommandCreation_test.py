# Теперь можем создать объект Shinobi, привязать к нему команду и выполнить ее
from Command import MoveForwardCommand, AttackCommand, CommandInvoker
from Ability import Ninjustu
from Shinobi import Shinobi

rasengan = Ninjustu("rasengan", 'ninjutsu', 100, 3, "no")
naruto = Shinobi(name="Naruto", abilities=[rasengan])

move_command = MoveForwardCommand(naruto)
attack_command = AttackCommand(naruto)

invoker = CommandInvoker(move_command)
invoker.action()

invoker.set_command(attack_command)
invoker.action()