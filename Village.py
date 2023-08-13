from abc import ABC, abstractmethod


class Village(ABC):
    def __init__(self, name, symbol, location):
        self.name = name
        self.symbol = symbol  # Эмблема или символ деревни
        self.location = location  # Географическое расположение

