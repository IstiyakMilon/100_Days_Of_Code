import math
def area(d, l):
  if d>l:
    a=l*l*(d*d-l*l) 
    # return a
    # return "{0:.2f}".format(math.sqrt(a))
    return round(math.sqrt(a), 2)
  else:
    return "Not a rectangle"

print(area(1,4))