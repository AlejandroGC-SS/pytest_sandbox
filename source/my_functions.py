def add(itemA,itemB):
  return itemA + itemB


def divide(itemA, itemB):
  if itemB == 0:
    raise ValueError('Item B cannot be zero in a division')
  return itemA / itemB