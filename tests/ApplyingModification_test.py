from Ability import Ninjustu
from Modification import ArmorModification
from Shinobi import Shinobi

rasengan = Ninjustu("rasengan", 'ninjutsu', 100, 3, "no")
naruto = Shinobi(name="Naruto", abilities=[rasengan])
armor = ArmorModification("armor", "armor increases health limit!")
print(f"Before adding armor: {naruto.health_limit}")
naruto.apply_modification(armor)
print(f"After adding armor: {naruto.health_limit}")
