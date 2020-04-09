def commonDivisors(a,b,c):
  list1=[]
  for i in range(1, min(a,b,c)+1):
    if a%i==0 and b%i==0 and c%i==0:
      list1.append(i)
  return list1

print(commonDivisors(16, 32, 96))

def getTotalX(a, b):
  results=[]
  for i in range(1,max(b)+1):
    if all(i%anum==0 for anum in a) and all(bnum%i==0 for bnum in b):
      results.append(i)
  return (len(results))