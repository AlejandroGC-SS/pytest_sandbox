import pytest
from source.square import Square

@pytest.mark.parametrize(
    "side_length,expected_area",
    [(5,25), (4,16), (9,81)]
)
def test_multiple_square_areas(side_length, expected_area):
  assert Square(side_length).area() == expected_area


@pytest.mark.parametrize(
    "side_length,expected_perimeter",
    [(3,12), (4,16), (9,36)]
)
def test_multiple_square_perimeters(side_length, expected_perimeter):
  assert Square(side_length).perimeter() == expected_perimeter