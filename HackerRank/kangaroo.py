def kangaroo(x1, v1, x2, v2):
  k1=x1
  k2=x2
  if x2>x1 and v2>v1:
    return "No"
  else:
    for i in range(10000):
      k1+=v1
      k2+=v2
      if k1==k2:
        return "Yes"
    return "No"

print(kangaroo(0, 2, 5, 3))