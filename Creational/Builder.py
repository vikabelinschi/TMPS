# Director   
class Director(object):
	def __init__(self):
		self.builder = None

	def prepare_burger(self):
		self.builder.new_burger()
		self.builder.choose_bun()
		self.builder.choose_meat()
		self.builder.choose_souce()
		self.builder.choose_cheese()
		return self.builder.burger

##################################

# Abstract Builder  
class Builder(object):
	def __init__(self):
		self.burger = None

	def new_burger(self):
		self.burger = Burger()

################################
from Creational.VegetarianBurger import *
# Concrete Builder

class Adapter(Builder):
	def choose_bun(self):
		self.burger.bun = VegetarianBurger.choose_bun(self)
	def choose_souce(self):
		self.burger.souce = VegetarianBurger.choose_sauce(self)
	def choose_meat(self):
		self.burger.meat = VegetarianBurger.choose_patty(self)
	def choose_cheese(self):
		self.burger.cheese = "None"

class BuilderBeconMonster(Builder):
	def choose_bun(self):
		self.burger.bun = 'Bun'

	def choose_meat(self):
		self.burger.meat = 'Beef Patty'

	def choose_souce(self):
		self.burger.souce = 'Ketchup'

	def choose_cheese(self):
		self.burger.cheese = 'Cheddar'

class BuilderChickenGrill(Builder):
	def choose_bun(self):
		self.burger.bun = 'Bun'

	def choose_meat(self):
		self.burger.meat = 'Chicken Fillet'

	def choose_souce(self):
		self.burger.souce = 'Mayo'

	def choose_cheese(self):
		self.burger.cheese = 'Parmegiano'

############################################

# Product
class Burger(object):
	def __init__(self):
		self.bun = None
		self.meat = None
		self.souce = None
		self.cheese = None

	def __repr__(self):
		return 'Bun: %s | Meat: %s | Souce: %s | Cheese: %s' % (self.bun, self.meat, self.souce, self.cheese)

#############################################

#Client
# if __name__ == "__main__":
# 	director = Director()
# 	director.builder = BuilderBeconMonster()
# 	burger = director.prepare_burger()
# 	print burger