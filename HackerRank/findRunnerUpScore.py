def runner_up_score(n, arr):
  finalArr=[]
  arr.sort()
  for i in range(n):
    if arr[i] not in finalArr:
      finalArr.append(arr[i])
  return finalArr[-2]


print(runner_up_score(5, [2, 3, 6, 6, 5]))