from firsttry.Characters.EntityFactory import EntityFactory
from firsttry.Characters.Shinobi import Shinobi


class ShinobiFactory(EntityFactory):
    def create_entity(self, config):
        return Shinobi(config["name"], config["health"], config["power"], config["taijutsu"], config["ninjutsu"], config["genjutsu"])
