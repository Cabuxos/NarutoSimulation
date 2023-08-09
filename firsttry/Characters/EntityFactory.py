from abc import ABC, abstractmethod


class EntityFactory(ABC):
    @abstractmethod
    def create_entity(self, config):
        pass