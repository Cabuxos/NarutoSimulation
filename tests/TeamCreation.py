from Jutsu import Ninjustu, Taijutsu
from Shinobi import Shinobi
from Team import Team

rasengan = Ninjustu("Rasengan", 'ninjutsu', 100, 3)
chidori = Ninjustu("Chidori", 'ninjutsu', 90, 5, "Lightning")
clonejutsu = Ninjustu("Clonejutsu", 'ninjutsu', 0, 3)
chakra_enhanced_strength = Taijutsu("Chakra Enhanced Strength", 'taijutsu', 50, 10)

naruto = Shinobi(name="Naruto", abilities=[rasengan, clonejutsu])
sasuke = Shinobi(name="Sasuke", abilities=[chidori, clonejutsu])
sakura = Shinobi(name="Sakura", abilities=[clonejutsu, chakra_enhanced_strength])
kakashi = Shinobi(name="Kakashi", abilities=[rasengan, chidori, clonejutsu])
# ino = Shinobi(name="Ino", abilities=[clonejutsu])


team7 = Team()
team7.name = "Team7"
team7.add_member(naruto)
team7.add_member(sasuke)
team7.add_member(sakura)
team7.add_member(kakashi)
team7.set_leader(kakashi)
team7.display_team()
