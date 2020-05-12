import math
a=1
b=2
c=1
bSquarMinus4ac=b*b-4*a*c
if bSquarMinus4ac<0:
  print("imaginary roots")
elif bSquarMinus4ac==0:
  # root=-b/2*a
  print(int(-b/2*a))
elif bSquarMinus4ac>0:
  root1=int((-b+math.sqrt(bSquarMinus4ac))/2*a)
  root2=int((-b-math.sqrt(bSquarMinus4ac))/2*a)
  print(root1, root2)

