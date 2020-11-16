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