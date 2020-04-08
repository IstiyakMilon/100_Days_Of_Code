def miniMaxSum(arr):
  arr.sort()
  minSum=0
  maxSum=0
  for i in arr[:4]:
    minSum+=i
  for i in arr[-4:]:
    maxSum+=i
  return (minSum, maxSum)

print(miniMaxSum([1,2,3,4,5]))