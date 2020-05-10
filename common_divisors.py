def common_divisor(a, b):
  n = 0
  divisorList=[]
  for i in range(1, min(a, b)+1): 
      if a%i==b%i==0: 
          n=i
          divisorList.append(n)
  print(*divisorList)

common_divisor(12,24)