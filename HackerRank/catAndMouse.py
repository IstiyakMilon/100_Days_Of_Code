def catAndMouse(x, y, z):
  catADist=abs(z-x)
  catBDist=abs(z-y)
  if catADist==catBDist:
    return "Mouse C"
  elif catADist<catBDist:
    return "Cat A"
  else:
    return "Cat B"

print(catAndMouse(1,2,3))
