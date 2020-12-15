from Creational.Command import *
from Creational.Builder import *
from Creational.Beverage import *
from Structural.Bridge import *
from Creational.VegetarianBurger import *
from Structural.Adapter import *
import time
from Behavioral.Strategy import *

class Waiter(object):
    def present_menu(self):
        print("Do you want a bussiness Lunch or to choose by yourself?")
        print("Press:")
        print("1 for Bussiness Lunch")
        print()
        print("2 for menu")
        print()

    def choose_menu(self, digit):
        if digit == 1:
            print("We have some interesting offers for you")
            self.bussiness_menu = BussinessLunchMenu()
            self.bussiness_menu.show_menu()
            self.bussiness_menu.command_to_kitchen()

        else:
            print("Our menu: ")
            self.whole_lunch = WholeMenu()
            self.whole_lunch.show_whole_menu()

#################################################

class BussinessLunchMenu(object):
    # def __init__(self):


    def show_menu(self):
        print()
        print("---------------------Lunch 1:-------------------")
        print("1. Cheese Burger", "Caesar Salad", "Juice", sep = " + ")
        print("---------------------Lunch 2:-------------------")
        print("2. Chicken Burger", "Tuna Salad", "Water", sep = " + ")
        print()
        print("Enter 1 or 2 for which you want")
        self.answer = int(input())

    def command_to_kitchen(self):
        if self.answer == 1:
            lunch = Lunch1() # receiver
            command_lunch = LunchCommand(lunch) # concrete command

            meal_invoker = MealInvoker(command_lunch); # invoker
            meal_invoker.invoke()

        if self.answer == 2:
            lunch2 = Lunch2() # receiver
            command_lunch2 = Lunch2Command(lunch2) # concrete command

            meal_invoker = MealInvoker(command_lunch2); # invoker
            meal_invoker.invoke()

        print("Thank you for choosing our restaurant")

#################################################

class WholeMenu(object):
    def show_whole_menu(self):
        print()
        print("Burgers:")
        print("1. Cheese Burger")
        print("2. Chicken Burger")
        print("3. Veggie Burger")
        print("-------------------------")
        print("Salads:")
        print("1. Caesar Salad")
        print("2. Tuna Salad")
        print("3. Shrimp Salad")
        print("-------------------------")
        print("Dressing:")
        print("1. Mayo")
        print("2. Olive Oil")
        print("3. Balsamic Sauce")
        print("-------------------------")

        print("Beverages:")
        print("1. Juice")
        print("2. Water")
        print("3. Coffee")
        print("4. Tea")
        print("-------------------------")
        print()
        print("Choose burger")
        self.answer = int(input())
        if self.answer == 1:
            director = Director()
            director.builder = BuilderBeconMonster()
            burger = director.prepare_burger()
            # print (burger)
        if self.answer == 2:
            director = Director()
            director.builder = BuilderChickenGrill()
            burger = director.prepare_burger()
        if self.answer == 3:
            director = Director()
            director.builder = Adapter()
            burger = director.prepare_burger()

        print("Choose Salad")
        self.answer = int(input())
        if self.answer == 1:
            print("Choose Dressing")
            self.answer = int(input())
            if self.answer == 1:
             salad = CaesarSalad(Mayo())
            if self.answer == 2:
             salad = CaesarSalad(OliveOil())
            if self.answer == 3:
             salad = CaesarSalad(BalsamicSauce)
        if self.answer == 2:
            print("Choose Dressing")
            self.answer = int(input())
            if self.answer == 1:
             salad = TunaSalad(Mayo())
            if self.answer == 2:
             salad = TunaSalad(OliveOil())
            if self.answer == 3:
             salad = TunaSalad(BalsamicSauce)
        if self.answer == 3:
            print("Choose Dressing")
            self.answer = int(input())
            if self.answer == 1:
             salad = ShrimpSalad(Mayo())
            if self.answer == 2:
             salad = ShrimpSalad(OliveOil())
            if self.answer == 3:
             salad = ShrimpSalad(BalsamicSauce())




        print("Choose Beverage")
        self.answer = int(input())
        if self.answer == 1:
            beverage = Beverage.factory_method("Juice")
        if self.answer == 2:
            beverage = Beverage.factory_method("Water")
        if self.answer == 3:
            beverage = Beverage.factory_method("Coffee")
        if self.answer == 4:
            beverage = Beverage.factory_method("Tea")

        print (burger)
        salad.add_dressing()
        beverage.get_beverage()
        print("Lunch is being made")
        

##################################################

if __name__ == "__main__":
    waiter = Waiter()
    print("================= Welcome to our restaurant ===============")
    print()
    print("Here is the menu:")
    waiter.present_menu()
    chosen_menu = int(input())
    waiter.choose_menu(chosen_menu)
    print("How do you want to pay?")
    print("1.Cash")
    print("2.Card")
    MenuPay.methods(Strategy)









