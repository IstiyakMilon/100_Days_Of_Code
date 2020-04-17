def divisibleSumPairs(n, k, ar):
  resultArr=[]
  for i in range(n-1):
    for j in range(i+1,n):
      if (ar[i]+ar[j])%k==0:
        resultArr.append([ar[i], ar[j]])
  return len(resultArr)

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))