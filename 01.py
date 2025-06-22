from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Рычание!"


class Monkey(Animal):
    def make_sound(self):
        return "Визг!"


class Elephant(Animal):
    def make_sound(self):
        return "Трубление!"


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass


class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()


class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()


class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()


def animal_sound_demo(factory: AnimalFactory):
    animal = factory.create_animal()
    print(f"Это животное издает звук: {animal.make_sound()}")
