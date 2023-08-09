from abc import ABC, abstractmethod


class Entity():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power  # Это может быть сила удара или базовая мощность для других типов персонажей

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} атакует {target.name} и наносит {self.power} урона!")

    def is_alive(self):
        return self.health > 0
