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
    def create_animal(self):
        pass


class LionFactory(AnimalFactory):
    def create_animal(self):
        return Lion()


class MonkeyFactory(AnimalFactory):
    def create_animal(self):
        return Monkey()


class ElephantFactory(AnimalFactory):
    def create_animal(self):
        return Elephant()


def interact_with_animal(factory):
    animal = factory.create_animal()
    sound = animal.make_sound()
    print(f"Звук: {sound}")


lion_factory = LionFactory()
monkey_factory = MonkeyFactory()
elephant_factory = ElephantFactory()

interact_with_animal(lion_factory)
interact_with_animal(monkey_factory)
interact_with_animal(elephant_factory)
