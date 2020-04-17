def commonDivisors(a,b,c):
  list1=[]
  for i in range(1, min(a,b,c)+1):
    if a%i==0 and b%i==0 and c%i==0:
      list1.append(i)
  return list1

print(commonDivisors(16, 32, 96))

def getTotalX(a, b):
  resultList=[]
  for i in range(1, max(b)+1):
    if all(i%numA==0 for numA in a) and all(numB%i==0 for numB in b):
      resultList.append(i)
  return (len(resultList))