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