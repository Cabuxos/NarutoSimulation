from __future__ import annotations
from Ability import Ninjustu, ChakraBoost
from Clan import Clan
from Shinobi import Shinobi
from Village import Village

rasengan = Ninjustu("rasengan", 'ninjutsu', 100, 3, "no")
konoha = Village(name="Hidden Leaf", symbol="Leaf Symbol", location="Fire Country")
shinobi = Shinobi(name="Naruto", abilities=[rasengan], clan=Clan(name="Uzumaki", description="Cool clan", jutsus=[], passive_abilities=[ChakraBoost]), team=None, village=konoha)

for ability in shinobi.abilities:
    print(f"{shinobi.name}'s name: {shinobi.name}")
    print(f"{shinobi.name}'s team: {shinobi.team}")
    print(f"{shinobi.name}'s clan: {shinobi.clan.name}")
    print(f"{shinobi.name}'s village: {shinobi.village.name}")
    print(f"{shinobi.name}'s country: {shinobi.village.location}")
    print(f"{shinobi.name} {ability.perform()}")
