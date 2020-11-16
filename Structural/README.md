#TMPS

Laboratory number 2 is a Structural Patern representation, using a restaurant association.

Author: Belinschi Victoria

To run from command line use:
python3 Client.py

## Main Tasks:

 1. By extending your project, implement atleast 3 structural design patterns in your project
    2. Keep your files grouped (into packages/directories) by their responsibilities (an example project structure)
    3. Document your work in a separate markdown file according to the requirements presented below (the structure can be extended of course)

## Theory:

 In software engineering, the Structural Design Patterns are concerned with how classes and objects are composed to form larger structures. 
 Structural class patterns use inheritance to create a hierarchy of classes/abstractions, but the structural object patterns use composition 
 which is generally a more flexible alternative to inheritance.

    Some examples of from this category of design patterns are :

Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

I used 3 of the mentioned patterns:
Adapter: structural design pattern that allows objects with incompatible interfaces to collaborate.
Bridge: structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction
and implementation—which can be developed independently of each other.
Decorator: structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that
contain the behaviors.

## Implementation
### Adapter
I used adapter to connect two incompatible interfaces : the burger Builder class and the VegetarianBurger class
As you see, the Adapter class converts the data from the VegetarianBurger class, making it compatible to the Builder class.
```python
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
```


