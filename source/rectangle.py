from source.shape import Shape
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  
  def __eq__(self, other):
    if not isinstance(other, Rectangle):
      return False
    return self.width == other.width and \
            self.length == other.length


  def area(self):
    return self.length * self.width


  def perimeter(self):
    return (self.length + self.width) * 2