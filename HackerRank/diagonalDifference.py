def diagonalDifference(arr):
  length=len(arr)
  sum1=0
  sum2=0
  for i in range(length):
    sum1+=arr[i][i]
    sum2+=arr[i][length-i-1]
  return abs(sum1-sum2)

print(diagonalDifference([[11, 2, 4],[4, 5, 6], [10, 8, -12]]))