from source.rectangle import Rectangle


def test_area(my_rectangle: Rectangle):
  assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle: Rectangle):
  assert my_rectangle.perimeter() == (10 + 20) * 2


def test_not_equals(my_rectangle: Rectangle, weird_rectangle: Rectangle):
  assert my_rectangle != weird_rectangle
