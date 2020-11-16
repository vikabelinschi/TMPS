import abc
from Creational.Builder import *
from Creational.Beverage import *
from Structural.Bridge import *

class Command(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

class LunchCommand(Command):
    def __init__(self, lunch):
        self.lunch = lunch

    def execute(self):
        self.lunch.make_lunch()

class Lunch2Command(Command):
    def __init__(self, lunch2):
        self.lunch2 = lunch2
        # self.price = price

    def execute(self):
        self.lunch2.make_lunch2()

class Lunch1:
    def make_lunch(self):
        director = Director()
        director.builder = BuilderBeconMonster()
        burger = director.prepare_burger()
        print (burger)

        print("Choose Dressing")
        self.answer = int(input())
        if self.answer == 1:
           salad = CaesarSalad(Mayo())
        if self.answer == 2:
           salad = CaesarSalad(OliveOil())
        if self.answer == 3:
           salad = CaesarSalad(BalsamicSauce)
        salad.add_dressing()

        beverage = Beverage.factory_method("Juice")
        beverage.get_beverage()
        print("Lunch is being made")


class Lunch2:
    def make_lunch2(self):
        director = Director()
        director.builder = BuilderChickenGrill()
        burger = director.prepare_burger()
        print("Lunch 2 is being made")
        print (burger)

        print("Choose Dressing")
        self.answer = int(input())
        if self.answer == 1:
             salad = TunaSalad(Mayo())
        if self.answer == 2:
             salad = TunaSalad(OliveOil())
        if self.answer == 3:
             salad = TunaSalad(BalsamicSauce)
        salad.add_dressing()

        beverage = Beverage.factory_method("Water")
        beverage.get_beverage()
        print("Lunch is being made")

class MealInvoker:
    def __init__(self, command):
        self.command = command
        # self.price = price

    def set_command(self, command):
        self.command = command
        # self.price = price

    def invoke(self):
        self.command.execute()

