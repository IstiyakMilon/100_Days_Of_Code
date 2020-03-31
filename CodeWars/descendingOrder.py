def descending_order(num):
  digitList=[]
  for x in str(num):
    x=int(x)
    digitList.append(x)

  digitList.sort(reverse=True)
  outputNum=""
  for i in digitList:
    i=str(i)
    outputNum+=i
  return int(outputNum)


inputNum=12345
print(descending_order(inputNum))