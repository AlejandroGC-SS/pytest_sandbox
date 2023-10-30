import pytest
import math
from source.circle import Circle
from source.rectangle import Rectangle


class TestCircle:
  def setup_method(self, method):
    print(f"setting up {method}")
    self.circle = Circle(radius=10)


  def teardown_method(self, method):
    print(f"tearing down {method}")


  def test_area(self):
    expected = math.pi * self.circle.radius ** 2
    print(f"area is {expected}")
    assert self.circle.area() == expected


  def test_perimeter(self):
    expected = math.pi * self.circle.radius * 2
    print(f"area is {expected}")
    assert self.circle.permieter() == expected

  def test_not_same_area_rectangle(self, my_rectangle: Rectangle):
    assert self.circle.area() != my_rectangle.area()
