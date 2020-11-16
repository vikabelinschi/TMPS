# TMPS

The first laboratory is a representation of Creational Paterns, using a restaurant association. 
I used Builder for the burger class, Factory method for beverages, abstract method for bussiness lunches .  

Author: Belinschi Victoria

To run the program run from commandline:

python3  Facade.py


## Main Tasks:
1. Choose an OO programming language and a suitable IDE or Editor (No frameworks/libs/engines allowed);

2. Select a domain area for the sample project;

3. Define the main involved classes and think about what instantiation mechanisms are needed;

4. Based on the previous point, implement atleast 3 creational design patterns in your project;

## Theory:
In software engineering, creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation.

**Abstract Factory**

Creates an instance of several families of classes

**Builder**

Separates object construction from its representation

**Factory Method**

Creates an instance of several derived classes

**Prototype**

A fully initialized instance to be copied or cloned

**Singleton**

A class of which only a single instance can exist

## Implementation:

In my code, I used three patterns for creating a prototype of a restaurant.

The Factory method for beverages:
```python
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
        print("Your water is done. You can take it.")

class Tea(Beverage):
    def get_beverage(self):
        print("Your tea is done. You can take it.")

class Coffee(Beverage):
    def get_beverage(self):
        print("Your coffee is done. You can take it.")
```

The Builder for burgers:
```python
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

# Abstract Builder  
class Builder(object):
	def __init__(self):
		self.burger = None

	def new_burger(self):
		self.burger = Burger()


# Concrete Builder
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

```

I used the Abstract method for creating bussiness lunches.

## Program Output:
![image](https://github.com/vikabelinschi/TMPS/blob/main/Screen%20Shot%202020-10-12%20at%2012.49.49.png)
![image](https://github.com/vikabelinschi/TMPS/blob/main/Screen%20Shot%202020-10-12%20at%2012.50.01.png)
![image](https://github.com/vikabelinschi/TMPS/blob/main/Screen%20Shot%202020-10-12%20at%2012.50.15.png)



