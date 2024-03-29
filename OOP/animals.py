"""
Сделать класс Pet абстрактным
"""
import random
import string
from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, age, master, weight, height):
        self.__name = name
        self.__age = age
        self.__master = master
        self.__weight = weight
        self.__height = height
        Pet.__counter += 1

    __counter = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def run(self, distance):
        print(f"Ran for {distance} meters")

    def jump(self, distance):
        print(f"Jumped {distance} meters")

    def sleep(self, time):
        print(f"Slept for {time} hours")

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height += height
        else:
            self.height += 0.2

    @abstractmethod
    def voice(self):
        raise NotImplementedError

    def __eq__(self, other):
        if self.age == other.age and self.height == other.height and self.weight == other.weight and self.__class__ == other.__class__:
            return True
        else:
            return False

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def get_random_name():
        letter = random.choice(string.ascii_uppercase)
        number = random.randint(1,99)
        return f"{letter}-{number}"


class Dog(Pet):
    def voice(self):
        print("Bark!")

    def jump(self, distance):
        if distance <= 0.5:
            super().jump(distance)
        else:
            print("Dogs cannot jump that far")


class Cat(Pet):
    def voice(self):
        print("Meow")

    def jump(self, distance):
        if distance <= 2:
            super().jump(distance)
        else:
            print("Cats cannot jump that far")


class Parrot(Pet):

    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.__species = species

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.05

    def fly(self, distance):
        if self.weight <= 0.1:
            print(f"Flew for {distance} meters")
        else:
            print("This parrot cannot fly.")

    def change_height(self, height=None):
        if height:
            self.height += height
        else:
            self.height += 0.05

    def jump(self, distance):
        if distance <= 2:
            super().jump(distance)
        else:
            print("Parrots cannot jump that far")

    def voice(self):
        print("squawk")


class Horse(Pet):
    def voice(self):
        print("Neigh")


class Donkey(Pet):
    def voice(self):
        print("hee-haw")


class Mule(Donkey, Horse):
    def voice(self):
        super().voice()
