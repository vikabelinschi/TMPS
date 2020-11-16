# TMPS

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

**Adapter**
**Bridge**
**Composite**
**Decorator**
**Facade**
**Flyweight**
**Proxy**

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


Adapter.py
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

VegetarianBurger.py
```python
class VegetarianBurger(object):
	def choose_bun(self):
	    self.burger.bun = "Brioche"
	    return self.burger.bun
	def choose_patty(self):
		self.burger.patty = "Veggy Patty"
		return self.burger.patty
	def choose_sauce(self):
		self.burger.sauce = "Ketchup"
		return self.burger.sauce
```

### Decorator
The decorator in my code has the role to add options to the beverage classes. So now,the client may choose if he wants lemon in the water,
coffee with milk or sugar in the tea.

Decorator.py
```python
class WithSugar:
  def __init__(self, Tea):
    self.Tea = Tea
    Tea.WithSugar = True
  
class WithMilk:
  def __init__(self, Coffee):
    self.Coffee = Coffee
    Coffee.WithMilk = True


class WithLemon:
  def __init__(self, Water):
    self.Water = Water
    Water.WithLemon = True

```

### Bridge
I used bridge to split the salad class, adding a dressing class which gives the client the posibility to choose mayo, olive oil or
balsamic sauce Dressing.

Bridge.py
```python
class Dressing:
    def fill_Dressing(self):
        pass

class Salad:
    def __init__(self, dressing):
        self.dressing = dressing

    def add_dressing(self):
        pass

class CaesarSalad(Salad):
    def __init__(self, dressing):
        super(CaesarSalad, self).__init__(dressing)

    def add_dressing(self):
        print("Caesar Salad with ", end="")
        self.dressing.fill_Dressing()

class TunaSalad(Salad):
    def __init__(self, dressing):
        super(TunaSalad, self).__init__(dressing)

    def add_dressing(self):
        print("Tuna Salad with ", end="")
        self.dressing.fill_Dressing()

class ShrimpSalad(Salad):
    def __init__(self, dressing):
        super(ShrimpSalad, self).__init__(dressing)

    def add_dressing(self):
        print("Shrimp Salad with ", end="")
        self.dressing.fill_Dressing()

class Mayo(Dressing):
    def fill_Dressing(self):
        print("mayo")

class OliveOil(Dressing):
    def fill_Dressing(self):
        print("OliveOil")

class BalsamicSauce(Dressing):
    def fill_Dressing(self):
        print("BalsamicSauce")
```
Client.py
```python
if self.answer == 1:
             salad = CaesarSalad(Mayo())
salad.add_dressing()
```

