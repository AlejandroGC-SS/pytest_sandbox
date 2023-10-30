import pytest
from source.rectangle import Rectangle

@pytest.fixture
def my_rectangle():
  return Rectangle(length=10,width=20)

@pytest.fixture
def weird_rectangle():
  return Rectangle(length=15,width=25)