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



class MenuPay:
    def methods(Strategy):
        chosen_pm = int(input())
        if chosen_pm == 1:
           context = Context(ConcreteStrategyA())
           context.do_some_business_logic()
        if chosen_pm == 2:
            context = Context(ConcreteStrategyB())
            context.do_some_business_logic()