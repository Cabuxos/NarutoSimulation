from firsttry.Characters.Entity import Entity
from firsttry.Characters.EntityFactory import EntityFactory


class CommonerFactory(EntityFactory):
    def create_entity(self, config):
        return Entity(config["name"], config["health"], config["power"])