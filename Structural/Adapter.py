from Creational.VegetarianBurger import*
from Creational.Builder import *

class Adapter(Builder):
	def choose_bun(self):
		self.burger.bun = VegetarianBurger.choose_bun(self)
		return self.burger.bun
	def choose_souce(self):
		self.burger.souce = VegetarianBurger.choose_sauce(self)
	def choose_meat(self):
		self.burger.meat = VegetarianBurger.choose_patty(self)
	def choose_cheese(self):
		self.burger.cheese = "None"
