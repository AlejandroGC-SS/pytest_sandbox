import pytest
import source.my_functions as my_functions
import time

def test_add():
  result = my_functions.add(1,2)
  assert result == 3


def test_divide():
  result = my_functions.divide(4,2)
  assert result == 2


def test_divide_by_zero():
  with pytest.raises(ValueError):
    my_functions.divide(10,0)


def test_add_strings():
  result = my_functions.add("habia una vez", " un niño muy sonriente")
  assert result == "habia una vez un niño muy sonriente"


@pytest.mark.slow
def test_very_slow():
  time.sleep(5)
  assert True

@pytest.mark.skip(reason='this feature is broken in this release')
def test_skipped_add():
  assert my_functions.add(1,2)

@pytest.mark.xfail(reason='we know we cannot divide by zero')
def test_divide_zero_broken():
  my_functions.divide(itemA=4,itemB=0)

