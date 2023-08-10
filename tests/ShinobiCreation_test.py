from Ability import Ninjustu
from Shinobi import Shinobi

rasengan = Ninjustu("rasengan", 'ninjutsu', 100, 3, "no")
naruto = Shinobi(name="Naruto", abilities=[rasengan])

for ability in naruto.abilities:
    print(f"{naruto.name} {ability.perform()}")
