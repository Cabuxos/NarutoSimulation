from firsttry.Characters.ShinobiFactory import ShinobiFactory
shinobi_config = {
    "name": "Наруто",
    "health": 100,
    "power": 10,
    "taijutsu": 5,
    "ninjutsu": 7,
    "genjutsu": 2
}

shinobi_factory = ShinobiFactory()
shinobi = shinobi_factory.create_entity(shinobi_config)
print(f"Shinobi name: {shinobi.name}")
print(f"Shinobi power: {shinobi.power}")