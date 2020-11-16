from Structural.Decorator import *
class Beverage(object):
    def factory_method(type):
        if type == "Juice":
            return Juice()
        if type == "Water":
            return Water()
        if type == "Tea":
            return Tea()
        if type == "Coffee":
            return Coffee()
    factory_method = staticmethod(factory_method)

class Juice(Beverage):
    def get_beverage(self):
        print("Your juice is done. You can take it.")

class Water(Beverage):
    def get_beverage(self):
        print("Do you want your water with lemon?")
        print("1.Yes")
        print("2.No")
        self.answer = int(input())
        if self.answer == 1:
          Water = WithLemon(self)
          print("Your water is done. You can take it.")
        if self.answer == 2:
          print("Your water is done. You can take it.")

class Tea(Beverage):
    def get_beverage(self):
        print("Do you want your tea with sugar?")
        print("1.Yes")
        print("2.No")
        self.answer = int(input())
        if self.answer == 1:
          Tea = WithSugar(self)
          print("Your tea is done. You can take it.")
        if self.answer == 2:
          print("Your tea is done. You can take it.")

class Coffee(Beverage):
    def get_beverage(self):
        print("Do you want your coffee with milk?")
        print("1.Yes")
        print("2.No")
        self.answer = int(input())
        if self.answer == 1:
          Coffee = WithMilk(self)
          print("Your coffee is done. You can take it.")
        if self.answer == 2:
          print("Your coffee is done. You can take it.")




   
