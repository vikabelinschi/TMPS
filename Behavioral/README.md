# TMPS

Laboratory number 3 is a Behavioral Patern representation, using a restaurant association.

Author: Belinschi Victoria

To run from command line use:
python3 Client.py

## Tasks

 1. By extending your project, implement as many behavioral design patterns as you need in your project
 
 
 2. Keep your files grouped (into packages/directories) by their responsibilities (an example project structure)


3. Document your work in a separate markdown file according to the requirements presented below (the structure can be extended of course)


## Theory

In software engineering, behavioral design patterns are design patterns that identify common communication patterns between objects and realize these patterns.
By doing so, these patterns increase flexibility in carrying out this communication.


**Chain of responsibility**

A way of passing a request between a chain of objects

**Command**

Encapsulate a command request as an object

**Interpreter**

A way to include language elements in a program

**Iterator**

Sequentially access the elements of a collection

**Mediator**

Defines simplified communication between classes

**Memento**

Capture and restore an object's internal state

**Null Object**

Designed to act as a default value of an object

**Observer**

A way of notifying change to a number of classes

**State**

Alter an object's behavior when its state changes

**Strategy**

Encapsulates an algorithm inside a class

**Template method**

Defer the exact steps of an algorithm to a subclass

**Visitor**

Defines a new operation to a class without change



## Implementation
### Strategy
I used the Strategy pattern to encapsulate the pay by cash & pay by card classes.


Strategy.py
```python
class Strategy(object):

    def do_algorithm(self):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self):
        print("Paying with cash")


class ConcreteStrategyB(Strategy):
    def do_algorithm(self):
        print("Paying by Card")


class Context():
    def __init__(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def do_some_business_logic(self) -> None:

        result = self._strategy.do_algorithm()
```

In the same file, i added a class for printing the results in order of the client's chosen option:

```python

class MenuPay:
    def methods(Strategy):
        chosen_pm = int(input())
        if chosen_pm == 1:
           context = Context(ConcreteStrategyA())
           context.do_some_business_logic()
        if chosen_pm == 2:
            context = Context(ConcreteStrategyB())
            context.do_some_business_logic()
 
 ```
 
 
 ## Program Output:
![image](https://github.com/vikabelinschi/TMPS/blob/master/Behavioral/ScreenShots/screenshot.png)
            

