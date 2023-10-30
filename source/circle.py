import math
from source.shape import Shape

class Circle(Shape):
  def __init__(self, radius):
    self.radius =  radius

  def area(self):
    return math.pi * (self.radius ** 2)

  def permieter(self):
    return math.pi * self.radius * 2