from Ability import Ninjustu
from Shinobi import Shinobi
from State import AttackingState, MeditatingState

rasengan = Ninjustu("rasengan", 'ninjutsu', 100, 3, "no")
naruto = Shinobi(name="Naruto", abilities=[rasengan])

naruto.handle()

naruto.set_state(AttackingState())
naruto.handle()

naruto.set_state(MeditatingState())
naruto.handle()