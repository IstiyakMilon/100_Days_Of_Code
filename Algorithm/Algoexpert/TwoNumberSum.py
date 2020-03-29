
#Define Two Number Sum function
def twoNumberSum(arr, targetSum):
  length=len(arr)
  twoNumber=[]
  for i in range(length):
    for j in range(i+1,length):
      if arr[i]+arr[j]==targetSum:
        twoNumber.append([arr[i], arr[j]])
  return twoNumber


list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]
inputSum=222
result=twoNumberSum(list, inputSum)
print(result)

