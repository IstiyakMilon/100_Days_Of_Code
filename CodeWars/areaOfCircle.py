from math import pi
def circleArea(r):
  
  if isinstance(r, str):
    return False
  elif r<1:
    return False
  else:
    r=float(r)
    return round(pi*r*r,2)